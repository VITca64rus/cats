from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash



app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@postgres:5432/sber'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
manager = LoginManager(app)

from sber import models, routes

#wa.whoosh_index(app,models.Cat)
# from fulltext import *
db.create_all()

from sber.models import User
me = User(login='root', password=generate_password_hash('root'))
db.session.add(me)
db.session.commit()
