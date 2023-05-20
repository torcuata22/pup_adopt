# import os
# from forms import AddForm, DelForm, AddOwnerForm
# from flask import Flask, render_template, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)

# app.config['SECRET_KEY']='mysecretekey'

# #SQL Database (for larger project use models.py)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# db = SQLAlchemy(app)
# Migrate(app,db)

# #Models:


    
# #view functions (moved to their respective folders):



# if __name__ == '__main__':
#     app.run(debug=True)


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