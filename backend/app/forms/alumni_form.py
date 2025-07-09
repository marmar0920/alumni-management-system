from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class AlumniForm(FlaskForm):
    fName = StringField('First Name', validators=[DataRequired(), Length(max=20)])
    lName = StringField('Last Name', validators=[DataRequired(), Length(max=20)])
    email = StringField('Email', validators=[Email(), Length(max=50)])
    phone = StringField('Phone', validators=[Length(max=10)])
    DOB = DateField('Date of Birth', format='%Y-%m-%d')
    gender = StringField('Gender', validators=[Length(max=1)])
    ethnicity = StringField('Ethnicity', validators=[Length(max=1)])
    website = StringField('Website', validators=[Length(max=100)])
    submit = SubmitField('Save')

