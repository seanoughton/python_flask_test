import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#the LoginManager class allows you to automate your login systems
from flask_login import LoginManager


login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
Migrate(app,db)

#pass in the app to the LoginManager
#this configures the app to have management of login users
login_manager.init_app(app)

#to tell users what view to go to when the log in
#there is a view called 'login'
login_manager.login_view = 'login'
