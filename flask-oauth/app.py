import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  #this sets up an environment variable
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

######################################################

from flask import Flask,redirect,url_for,render_template
from flask_dance.contrib.google import make_google_blueprint,google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

blueprint = make_google_blueprint(client_id='751961054763-vjku83vbtca9lju7l7b9jad9g41jl7u1.apps.googleusercontent.com',client_secret='sMIjUNX4OxfztNqQxqNpx-Qh',offline=True,scope=['profile','email'])

app.register_blueprint(blueprint,url_prefix='/login') #this syncs the login to go to google to login


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    #THIS WILL RETURN AN INTERNAL SERVER ERROR IF THE USER IS NOT LOGGED IN
    resp = google.get('/oauth2/v2/userinfo') #if the user is logged in with google
    assert resp.ok,resp.text #this checks to see if the response is ok
    #you can get data from the response from google
    email = resp.json()['email'] #this gets the email key/value from the json response

    return render_template('welcome.html',email=email)


@app.route('/login/google')
def login():
    if not google.authorized: #this works because of importing flask.dance.contrib.google
        return render_template(url_for('google.login')) #this takes you to login with google

    resp = google.get('/oauth2/v2/userinfo') #if the user is logged in with google
    assert resp.ok,resp.text #this checks to see if the response is ok
    #you can get data from the response from google
    email = resp.json()['email'] #this gets the email key/value from the json response

    return render_template('welcome.html',email=email)

if __name__ == '__main__':
    app.run()
