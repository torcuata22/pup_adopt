import os
from forms import AddForm, DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY']='mysecretekey'

#SQL Database (for larger project use models.py)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
Migrate(app,db)

#Models:






    
#view functions (they use forms):

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()
    if form.validate():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html', form=form)

@app.route('/add_owner', methods=['GET','POST'])
def add_owner():
    form = AddOwnerForm()
    if form.validate():
        name = form.name.data
        pup_id = form.pup_id.data
        new_owner = Owner(name, pup_id)
        db.session.add(new_owner)
        db.session.commit()    

        return redirect(url_for('list_pup'))
    return render_template('add_owner.html',form=form)


@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=['GET','POST'])
def del_pup():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html', form = form)



if __name__ == '__main__':
    app.run(debug=True)


#create flask app:  export FLASK_APP=adoption_site.py
#initialize db: flask db init 
#flask db migrate -m "new tables"
#flask db upgrade

#blueprints library wil register url prefix for each views.py file when we refactor
#/owners/add and /puppies/add
#Refactor:
#Restructure project folders
#Add blueprints
#register Blueprints in __init__.py
# __init__.py contains all the information that creates the application