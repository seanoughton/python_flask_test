from myproject import app,db
from flask import render_template,redirect,url_for,flash,abort,request

#you can decorate the view functions with these
from flask_login import login_user,login_required,logout_user

from myproject.models import User
from myproject.forms import LoginForm,RegistrationForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required #this makes sure that in order to see this view the user is loggedin
def welcome_user():
    return render_template('welcome_user.html')


@app.route('/logout')
@login_required
def logout():
    logout_user() #from flask login
    flash('You logged out')
    return redirect(url_for('home'))

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        #this makes sure that a user is supplied and that the password is correct
        if user.check_password(form.password.data) and user is not None:
            login_user(user) #imported login_user from flask_login
            flash('Logged in Successfully!')

            #if a user was trying to visit a page that required login, and was then taken to the login screen, you can save the page that the user was trying to go to as next
            #flask saves the request for that page as next
            next = request.args.get('next')
            #check if next exists or go to the welcome page
            if next == None or not next[0]=='/':
                next = url_for('welcome_user')

            #redirect to whatever url is in next
            return redirect(next)
    return render_template('login.html',form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash("Thanks for registering!")
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
