from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class EmploymentForm(FlaskForm):
    companyName = StringField('Company Name', validators=[DataRequired(), Length(max=100)])
    jobTitle = StringField('Job Title', validators=[DataRequired(), Length(max=100)])
    startDate = DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    endDate = DateField('End Date', format='%Y-%m-%d')
    currentYN = SelectField('Current?', choices=[('Y', 'Yes'), ('N', 'No')], validators=[DataRequired()])
    primaryYN = SelectField('Primary?', choices=[('Y', 'Yes'), ('N', 'No')], validators=[DataRequired()])
    submit = SubmitField('Save')

