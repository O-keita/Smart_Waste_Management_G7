from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b7318d5b51927a4dc8f7fad696408fc4'
# mysql db to be connected to after everything is done
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Okeita:mansaring@Okeita.mysql.pythonanywhere-services.com/Okeita$SmartWaste'

#sqlite db for text editor
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
admin = Admin(app)

from app import routes