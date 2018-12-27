from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

#CREATING THE OWNERS Blueprint
owners_blueprint = Blueprint('owners',
                              __name__,
                              template_folder='templates/owners')

@owners_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        # Add new owner to database
        new_owner = Owner(name,pup_id)
        db.session.add(new_owner)
        db.session.commit()

        #puppies.list is the view function called list within the puppies views
        #you call it this way because the views will be registered with a blueprint, so our are saying get me the list function(route,view) in the puppies view file, redirect there
        return redirect(url_for('puppies.list'))
    return render_template('add_owner.html',form=form)
