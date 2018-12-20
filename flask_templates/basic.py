from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # name = "Jose"
    # letters = list(name)
    # pup_dictionary = {'pup_name':'sammy'}
    # return render_template('basic.html',name = name,letters = letters, pup_dictionary = pup_dictionary)
    mylist = [1,2,3,4,5]
    puppies = ['snoopy','spike','fido']
    return render_template('basic.html', mylist=mylist, puppies = puppies)


if __name__ == '__main__':
    app.run(debug=True)
