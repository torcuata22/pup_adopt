import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
Migrate(app,db)

#after all of the aboe is done, I need to register the blueprint
