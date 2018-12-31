import os
from forms import AddFormPup,AddFormOwner,DelForm

from flask import Flask, render_template,url_for,request,redirect

#import the ORM and the migration module
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecretkey"

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app) #this creates the db by passing in the app to SQLAlchemy
Migrate(app,db) #this gives the ability to migrate, connecting the app with the database


################### models ##########################
class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Puppy name: {self.name}"

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    # We use puppies.id because __tablename__='puppies'
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

################### models ##########################


#################### views ############################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addpup',methods=['GET','POST'])
def add_pup():
    form = AddFormPup()

    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pup'))


    return render_template('addpuppy.html',form=form)

@app.route('/addowner',methods=['GET','POST'])
def add_owner():
    form = AddFormOwner()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.id.data
        new_owner = Owner(name,pup_id)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('list_owners'))


    return render_template('addowner.html',form=form)

@app.route('/delete',methods=['GET','POST'])
def delete_pup():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('deletepuppy.html',form=form)

@app.route('/puppylist')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('listpuppies.html',puppies=puppies)

@app.route('/ownerlist')
def list_owners():
    owners = Owner.query.all()
    info = {}
    count = 1
    for owner in owners:
        id = owner.puppy_id
        print(id)
        info[owner.name] =  Puppy.query.get(2).name

    return render_template('listowners.html',owners=owners,info=info)

#################### views ############################




if __name__ == '__main__':
    app.run(debug=True)
