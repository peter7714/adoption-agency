from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import NumberRange, AnyOf, URL, Optional

class AddPetForm(FlaskForm):
    name = StringField('Name')
    species = StringField('Species', validators=[AnyOf(['Dog', 'Cat', 'Komodo Dragon'], message='Must be Dog, Cat or Komodo Dragon')])
    photo_url = StringField('Picture', validators=[Optional(), URL(require_tld=True, message='Must be a Valid URL')])
    age = FloatField('Age', validators=[NumberRange(min=0, max=30, message='Must be between 0 and 30')])
    notes = StringField('Pet Notes')

class EditPetForm(FlaskForm):
    photo_url = StringField('Picture', validators=[Optional(), URL(require_tld=True, message='Must be a Valid URL')])
    notes = StringField('Pet Notes')
    available = BooleanField('Available')