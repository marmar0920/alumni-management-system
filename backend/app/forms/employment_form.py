from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class EmploymentForm(FlaskForm):
    alumniID = IntegerField('Alumni ID', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired(), Length(max=100)])
    city = StringField('City', validators=[Length(max=50)])
    state = StringField('State', validators=[Length(max=2)])
    zip = StringField('Zip Code', validators=[Length(max=10)])
    jobTitle = StringField('Job Title', validators=[DataRequired(), Length(max=100)])
    startDate = DateField('Start Date', format='%Y-%m-%d')
    endDate = DateField('End Date', format='%Y-%m-%d')
    currentYN = SelectField('Is Current?', choices=[('Y', 'Yes'), ('N', 'No')], validators=[DataRequired()])
    submit = SubmitField('Save')

