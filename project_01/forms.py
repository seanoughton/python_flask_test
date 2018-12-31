from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddFormPup(FlaskForm):

    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')


class AddFormOwner(FlaskForm):

    name = StringField('Name of Owner: ')
    id = IntegerField('Puppy Id')
    submit = SubmitField('Add Owner')


class DelForm(FlaskForm):

    id = IntegerField("Id Number of Puppy to Remove: ")
    submit = SubmitField("Remove Puppy")
