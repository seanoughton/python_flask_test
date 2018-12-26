from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import  (StringField,BooleanField,SubmitField,DateTimeField,
                        RadioField,SelectField,TextField,TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you?',validators=[DataRequired()])
    #validators is a list of validator objects
    #this creates an instance of DataRequired object to pass into validators
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField('Please choose your mood:',
                        choices=[('mood_one','Happy'),('mood_two','Excited')])
    #choices are a list of tuple pairs, which give a value and a lable
    #in this case the label is mood_one, and the value is label

    food_choice = SelectField(u'Pick your favorite food:',
                                choices=[('chi','Chicken'),('bf','Beef'),('fish','Fish')])
    #the u forces this to be a unicode string
    #Chicken is what the users sees, and and the backend we call it chi for short

    feedback = TextAreaField()

    submit = SubmitField('Submit')


@app.route('/',methods=['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))
    return render_template('index.html',form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
