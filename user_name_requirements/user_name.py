from flask import Flask, render_template, request
#request grabs the information from the html form

#3 requirements
# 1 must contain a lowercase letter
# 2 must contain an uppercase letter
# 3 must end in a number

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reports')
def reports():
    username = request.args.get('username')
    errors = []
    #runs some checks and issue a response
    if not any(x.isupper() for x in username):
        errors.append('You did not use an upper case letter.')
    if not any(x.islower() for x in username):
        errors.append('You did not use a lower case letter.')
    if not username[-1].isdigit():
        errors.append('Your did not end your username with a number.')

    return render_template('reports.html',errors=errors)



if __name__ == '__main__':
    app.run(debug=True)
