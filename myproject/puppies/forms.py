from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Puppy Name: ')
    submit=SubmitField('Add Puppy')


class DelForm(FlaskForm):
    id=IntegerField("Id number of Puppy to remove")
    submit = SubmitField("Remove Puppy")