from flask import render_template, request, redirect, flash, url_for, jsonify
from flask_login import login_user, login_required
from werkzeug.security import check_password_hash
from sber.models import User, Cat
from sber import app, db
from sber.full_text_search import create_connection, execute_read_query


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get ('password')
    if login and password:
        user = User.query.filter_by(login=login).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page)
        else:
            flash('Login or password is not correct')
    else:
        flash('Please fill login and password fields')
    return render_template("login.html")


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


def get_result_for_id(cat_id):
    result = []
    qre = Cat.query.filter_by(id=cat_id).first()
    if qre:
        result.append({'id': qre.id, 'name': qre.name, 'age': qre.age, 'info': qre.info, 'breed': qre.breed,
                       'photo': qre.photo})
    return result


def get_result_for_sort(sort):
    result = []
    if sort == '1' or (sort is None):
        qre = Cat.query.order_by(Cat.name)
    elif sort == '2':
        qre = Cat.query.order_by(Cat.breed)
    elif sort == '3':
        qre = Cat.query.order_by(Cat.age)
    else:
        return result
    for i in qre:
        result.append({'id': vars(i)['id'], 'name': vars(i)['name'], 'age': vars(i)['age'],
                       'info': vars(i)['info'], 'breed': vars(i)['breed'], 'photo': vars(i)['photo']})
    return result


@app.route('/list', methods=['GET'])
def get_list():
    cat_id = request.args.get('id')
    sort = request.args.get('sort')
    find = request.args.get('find')
    if cat_id:
        return jsonify(get_result_for_id(cat_id))
    elif sort and find:
        connect = create_connection("sber", "postgres", "root", "127.0.0.1", "5432")
        if connect:
            if sort == '1' or (sort is None):
                info = execute_read_query(connect, find, 'name')
            elif sort == '2':
                info = execute_read_query (connect, find, 'breed')
            elif sort == '3':
                info = execute_read_query (connect, find, 'age')
            else:
                return jsonify([])
            connect.close()
        return jsonify(info)
    else:
        return jsonify(get_result_for_sort(sort))
    return jsonify([])


@app.after_request
def redirect_to_sign(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)
    return response
