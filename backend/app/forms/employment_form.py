from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Optional

class EmploymentForm(FlaskForm):
    alumniID = IntegerField('Alumni ID', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired(), Length(max=100)])
    city = StringField('City', validators=[Optional(), Length(max=50)])
    state = StringField('State', validators=[Optional(), Length(max=2)])
    zip = StringField('Zip Code', validators=[Optional(), Length(max=10)])
    jobTitle = StringField('Job Title', validators=[DataRequired(), Length(max=100)])
    startDate = DateField('Start Date', format='%Y-%m-%d', validators=[Optional()])
    endDate = DateField('End Date', format='%Y-%m-%d', validators=[Optional()])
    currentYN = SelectField('Is Current?', choices=[('Y', 'Yes'), ('N', 'No')], validators=[DataRequired()])
    primaryYN = SelectField('Primary Employment?', choices=[('Y', 'Yes'), ('N', 'No')], validators=[DataRequired()])
    submit = SubmitField('Save')


