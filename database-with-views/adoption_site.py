import os
from forms import AddForm,DelForm

#import flask and the modules used
from flask import Flask,render_template,url_for,redirect

#import the ORM and the migration module
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__) #creates the app and names it the name of the file

app.config['SECRET_KEY'] = 'mysecretkey' #this is for CSRF for the forms

####################### SQL Database ###########################

basedir = os.path.abspath(os.path.dirname(__file__)) #sets the file path for this file
#config the database with the ORM, gives the path to the database file
#tells it not to track all modifications to the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db = SQLAlchemy(app) #this creates the db by passing in the app to SQLAlchemy
Migrate(app,db) #this gives the ability to migrate, connecting the app with the database
####################### SQL Database ###########################

####################### MODELS ###########################

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Puppy name: {self.name}"

####################### MODELS ###########################

####################### VIEWS ###########################

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add',methods=['GET','POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    #the default view for add_pup should go to the add page
    return render_template('add.html',form=form)



@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html',puppies=puppies)


@app.route('/delete',methods=['GET','POST'])
def del_pup():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('delete.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
