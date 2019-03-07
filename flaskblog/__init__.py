import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '45385b37d4fd30237a8f76696fba1bf3'
# The following configuration of SQLITE is for windows only
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\Projects\\FlaskBlog\\temp\\data.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

#Setup mail server before deploying
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config["MAIL_USE_SSL"] = True
app.config['MAIL_USERNAME'] = os.environ.get('GMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('GMAIL_PASS')
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_PORT'] = 587
mail = Mail(app)

from flaskblog import routes