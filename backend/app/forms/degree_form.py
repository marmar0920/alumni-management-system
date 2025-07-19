from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class DegreeForm(FlaskForm):
    alumniID = IntegerField('Alumni ID', validators=[DataRequired()])
    degreeType = SelectField(
        'Degree Type',
        choices=[
            ('BA', 'Bachelor of Arts'),
            ('BS', 'Bachelor of Science'),
            ('MA', 'Master of Arts'),
            ('MS', 'Master of Science'),
            ('PhD', 'Doctor of Philosophy'),
            ('Other', 'Other'),
        ],
        validators=[DataRequired()]
    )
    major = StringField('Major', validators=[DataRequired(), Length(max=50)])
    minor = StringField('Minor', validators=[Length(max=50)])
    graduationDate = DateField('Graduation Date', format='%Y-%m-%d')
    conferredDate = DateField('Conferred Date', format='%Y-%m-%d')
    university = StringField('University', validators=[Length(max=100)])
    city = StringField('City', validators=[Length(max=50)])
    state = StringField('State', validators=[Length(max=2)])
    primaryYN = SelectField(
        'Primary Degree?',
        choices=[('Y', 'Yes'), ('N', 'No')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Save')