from companyblog import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
#gives you functionality like, is authenticated, is active on the model inside the templates
from flask_login import UserMixin
from datetime import datetime

#USER AUTHENTICATION
#THIS ALLOWS FLASK TO LOAD THE CURRENT USER AND GRAB THEIR ID
#this loads in the current user and allows you to use that in the templates
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique=True,index=True)
    #index = True allows you to make that column into an index that you can use
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('BlogPost',backref='author',lazy=True)

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'Username {self.username}'

class BlogPost(db.Model):


    users = db.relationship(User)

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    title = db.Column(db.String(140),nullable=False)
    text = db.Column(db.Text,nullable=False)


    def __init__(self,title,text,user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f'Post ID: {self.id} --Date: {self.date} -- Title: {self.title}'
