from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user,current_user,logout_user,login_required
from companyblog import db #this says go to the main __init__.py file and grab the db instance that was created
from companyblog.models import User,BlogPost
from companyblog.users.forms import RegistrationForm,LoginForm,UpdateUserForm
from companyblog.users.picture_handler import add_profile_pic #this grabs the function from this file

users = Blueprint('users',__name__)


@users.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm() #creates an instance of the registration form

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        # flash('Thanks for Registering')
        return redirect(url_for('users.login'))

    return render_template('register.html',form=form)

@users.route("/logout")
def logout():
    logout_user() #this comes from flask_login
    return redirect(url_for('core.index'))


@users.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and users is not None:
            login_user(user)
            flash('Log in Success!')
            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('core.index')
            return redirect(next)

    return render_template('login.html',form=form)


@users.route('/account',methods=['GET','POST'])
@login_required
def account():
    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data: #if they actually uploaded some picture data
            username = current_user.username
            pic = add_profile_pic(form.picture.data.username)
            #form.picture.data gets the actual image file
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit
        # flash('User Account Updated')
        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    #this grabs the profile image from the static folder with the current_users profile image name
    profile_image = url_for('static',filename='profile_pics/'+current_user.profile_image)

    return render_template('account.html',profile_image=profile_image,form=form)

@users.route('/<username>')
def user_posts():
    #this will allow you to cycle through user posts using pages
    page = request.args.get('page',1,type=int)
    #this allows you to return a 404 error if the user types in the name wrong
    user = User.query.filter_by(username=username).first_or_404()
    #the foreign key for a blogpost is backreferenced to author (not user)
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
    #paginate allows you to have pages, and limit the blog posts per page
    return render_template('user_blog_posts.html',blog_posts=blog_posts,user=user)
