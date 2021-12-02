from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CreatelocationForm(FlaskForm):
    country_name = StringField("Which country is this gallery located in?", validators=[DataRequired()])
    city = StringField("Which city is this gallery located in?", validators=[DataRequired()])
    submit = SubmitField("Submit location!")



class CreategalleryForm(FlaskForm):
    gallery_name = StringField("Name of gallery:", validators=[DataRequired()])
    information = StringField("Genre of gallery:", validators=[DataRequired()])
    fee = StringField("Is there a fee for this gallery?", validators=[DataRequired()])
    locations = SelectField("Select city of where yout gallery is located:", choices=[], validators=[DataRequired()])
    submit = SubmitField("Submit gallery!")
