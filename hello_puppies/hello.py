from flask import Flask #import flask class
app = Flask(__name__) # creates an app object as an instance of the class Flask
## __name__ is a python predefined variable, which is then set to the name of the module in which it is used
# this tells us ... are we running this script directly, or within another script where it is imported

@app.route('/') ## this is a decorator that defines the route
def index():
    return '<h1>Hello Puppy!</h1>'


@app.route('/information')
def info():
    return "Puppies are cute."

@app.route('/puppy/<name>')
def puppy(name):
    # return '<h1>This is a page for {}</h1>'.format(name)
    # return '<h1>This is a page for {}</h1>'.format(name.upper())
    return '<h1>100th letter: {}</h1>'.format(name)[100]
#if you are running this script directly, then run your application
if __name__ == '__main__':
    app.run(debug=True)
