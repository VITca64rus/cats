from flask_login import UserMixin
from sber import db, manager, app


class User (db.Model, UserMixin):
    id = db.Column (db.Integer, primary_key=True)
    login = db.Column (db.String (128), nullable=False, unique=True)
    password = db.Column (db.String (255), nullable=False)


class Cat (db.Model):
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String (128), nullable=False)
    age = db.Column (db.Integer, nullable=False)
    info = db.Column (db.String, nullable=False)
    breed = db.Column (db.String (255))
    photo = db.Column (db.String)


@manager.user_loader
def load_user(user_id):
    return User.query.get (user_id)