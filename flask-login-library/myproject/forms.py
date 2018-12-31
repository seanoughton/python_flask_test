from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
#the validators can be pass in to instances of StringField,PasswordField,SubmitField
#DataRequired - can't leave field blank
#Email - checks email format to make sure it is proper email format
#EqualTo - password confirmation, confirms user password with second field
from wtforms import ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Log in")

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match!')])
    #this checks to make sure that the two passwords are equal to each other
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

    #check to see if the email has already been used by another user
    def check_email(self,field):
        if User.query.filter_by(email=field.data.first()):
            raise ValidationError('Your email has been already registered!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is taken!')
