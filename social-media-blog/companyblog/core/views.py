from flask import render_template,request,Blueprint

#this registers the componet(view) with the Flask app through the Blueprint module
#blueprints map to the route  for 'core'
#blueprints register a url prefix for 'core', that maps to these views
#the blueprints are actually registered in the main __init__.py file
#allows you to use decorators with the name of the component
core = Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template('index.html')


@core.route('/info')
def info():
    return render_template('info.html')
