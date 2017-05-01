from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import views, models

import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir
# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
