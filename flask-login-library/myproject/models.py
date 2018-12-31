from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
#from inheriting from the UserMixin class, you get a lot of attributes that you will be able to call in the views

#THIS WILL ALLOW FLASK LOGIN TO LOAD THE CURRENT USER AND GRAB THEIR ID
#ALLOWS YOU TO SHOW SPECIFIC PAGES BASED ON THE USER ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    #loads the current user based on their id
    #allows you to call current_user in your templates

#UserMixin has all of the management features of logging in and authorizing users
class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True) #limits the number of characters and forces a unique email
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    #RETURN TRUE OR FALSE FOR CHECKING THE PASSWORD
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
