 #if a name does not end in a y, add a y
 # if a name does end in a y, replace it with iful instead


from flask import Flask
app = Flask(__name__)

@app.route('/') ## this is a decorator that defines the route
def index():
    return '<h1>Hello Puppy!</h1>'


@app.route('/information')
def info():
    return "Puppies are cute."

@app.route('/puppy_latin/<name>')
def puppy(name):
    if name[-1] == "y":
        latin_name = name[:-1] + "iful"
    else:
        latin_name = name + "y"
    return '<h1>Hi {}! Your puppylatin name is {}</h1>'.format(name,latin_name)


if __name__ == '__main__':
    app.run(debug=True)
