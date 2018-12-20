import os #os allows you to grab directory names and filepath names with python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #pip install Flask-Migrate


basedir = os.path.abspath(os.path.dirname(__file__))
#when a module is loaded in python this __file__ variable is built in and that is set to the name of the actual file
# this means that __file__ is set to basic.py
# os.path.dirname(__file__) is getting the directory name that the basic.py file is located int, flask/databases/basic.py
# os.path.abspath(os.path.dirname(__file__)) this gets the absolute path for the directory
# /Users/seanoughton/code/udemy/flask/databases
#this prevents you from having to manually typing the path and works across operating systems
#print (basedir)

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)



#######################################
#MODELS
#######################################

class Puppy(db.Model): #the name of the class will be the name of model and the name of the table in the db

    __tablename_ = "puppies" #manual override table name

    #create the columns for the __table
    id = db.Column(db.Integer, primary_key=True) #this creates a column for id in the table which will have integer values, and also setting this to be the primary key for the table
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self,name,age,breed): #initialize method for the class
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self): #the string representation of the object created
        return f"Puppy {self.name} is {self.age} year/s old"
