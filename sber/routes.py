from flask import render_template, request, redirect, flash, url_for, jsonify
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash
import os
from sber.models import User, Cat
from sber.forms import LoginForm
from sber import app
from sber.full_text_search import create_connection, execute_read_query


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        user = User.query.filter_by(login=login).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return render_template("cats.html")
        else:
            logout_user()
            flash('Login or password is not correct')
    return render_template("login.html", form=form)


@app.route('/admin/cat')
@login_required
def cat_page():
    return render_template("cat.html")


@app.route('/admin/cats')
@login_required
def cats():
    return render_template("cats.html")


@app.route('/')
@login_required
def index():
    return render_template("index.html")


def ft_create_list_dict(res):
    result = []
    if res:
        for i in res:
            result.append({'id': vars(i)['id'], 'name': vars(i)['name'],
                           'age': vars(i)['age'], 'info': vars(i)['info'],
                           'breed': vars(i)['breed'],
                           'photo': vars(i)['photo']})
    return result


def ft_select_id(cat_id):
    result = []
    qre = Cat.query.filter_by(id=cat_id).first()
    if qre:
        result.append({'id': qre.id, 'name': qre.name, 'age': qre.age,
                       'info': qre.info, 'breed': qre.breed,
                       'photo': qre.photo})
    return result


def ft_select_sort(sort):
    res = None
    if sort == '1' or (sort is None):
        res = Cat.query.order_by(Cat.name)
    elif sort == '2':
        res = Cat.query.order_by(Cat.breed)
    elif sort == '3':
        res = Cat.query.order_by(Cat.age)
    return ft_create_list_dict(res)


def ft_select_sort_find(sort, find):
    res = None
    connect = create_connection("sber", os.environ['USER_DB'],
                                os.environ['PASSWORD_DB'],
                                "postgres", "5432")
    if sort == '1' or (sort is None):
        res = execute_read_query(connect, find, 'name')
    elif sort == '2':
        res = execute_read_query(connect, find, 'breed')
    elif sort == '3':
        res = execute_read_query(connect, find, 'age')
    connect.close()
    return res


@app.route('/list', methods=['GET'])
def get_list():
    cat_id = request.args.get('id')
    sort = request.args.get('sort')
    find = request.args.get('find')
    if cat_id:
        return jsonify(ft_select_id(cat_id))
    elif sort and find:
        return jsonify(ft_select_sort_find(sort, find))
    else:
        return jsonify(ft_select_sort(sort))


@app.after_request
def redirect_to_sign(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)
    return response
