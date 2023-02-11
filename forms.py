from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class AddPetForm(FlaskForm):
    name = StringField('Name')
    species = StringField('Species')
    img = StringField('Picture')
    age = FloatField('Age')
    notes = StringField('Pet Notes')
    