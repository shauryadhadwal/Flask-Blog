from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '45385b37d4fd30237a8f76696fba1bf3'
# The following configuration of SQLITE is for windows only
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\Projects\\FlaskBlog\\temp\\data.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

from flaskblog import routes