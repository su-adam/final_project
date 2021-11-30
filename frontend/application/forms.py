from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LocationForm(FlaskForm):
    location = SelectField("Location in London", choices[])
    submit = SubmitField("Submit location")

