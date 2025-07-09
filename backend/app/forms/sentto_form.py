from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, SubmitField
from wtforms.validators import DataRequired

class SenttoForm(FlaskForm):
    newsletterID = SelectField('Newsletter', coerce=int, validators=[DataRequired()])
    alumniID = SelectField('Alumnus', coerce=int, validators=[DataRequired()])
    sentDate = DateField('Sent Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Save')

