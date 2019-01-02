from flask import render_template,request,Blueprint
from companyblog.models import BlogPost

#this registers the componet(view) with the Flask app through the Blueprint module
#blueprints map to the route  for 'core'
#blueprints register a url prefix for 'core', that maps to these views
#the blueprints are actually registered in the main __init__.py file
#allows you to use decorators with the name of the component
core = Blueprint('core',__name__)

@core.route('/')
def index():
    page = request.args.get('page',1,type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
    return render_template('index.html',blog_posts=blog_posts)


@core.route('/info')
def info():
    return render_template('info.html')
