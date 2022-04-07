from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + \
                                        os.environ['USER_DB'] + ':' + \
                                        os.environ['PASSWORD_DB'] + \
                                        '@postgres:5432/sber'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
manager = LoginManager(app)
