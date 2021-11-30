from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LocationForm(FlaskForm):
    location = SelectField("Location in London", choices=[])
    submit = SubmitField("Submit location")


class Createlocation(FlaskForm):
    name 
    submit 
    country

class Creategallery(Flaskform):
    location = SelectField("Location in London", choices=[])
    submit = SubmitField("Submit location")
    # selectfield for location

# create another form which allows users to add to gallery table also to add