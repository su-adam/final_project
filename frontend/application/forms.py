from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CreatelocationForm(FlaskForm):
    location = SelectField("Location in London", choices=[])
    country = StringField("Which country is this gallery located in?", validators=[DataRequired()])
    city = StringField("Which city is this gallery located in?", validators=[DataRequired()])
    submit = SubmitField("Submit location!")



class CreategalleryForm(FlaskForm):
    name = StringField("Name of gallery:", validators=[DataRequired()])
    information = StringField("Genre of gallery:", validators=[DataRequired()])
    fee = StringField("Is there a fee for this gallery?", validators=[DataRequired()])
    submit = SubmitField("Submit gallery!")
