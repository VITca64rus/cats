from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import flask_whooshalchemy as wa
from flask_login import LoginManager



app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/sber'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
manager = LoginManager(app)

from sber import models, routes

#wa.whoosh_index(app,models.Cat)
from fulltext import *
db.create_all()