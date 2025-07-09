from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class DegreeForm(FlaskForm):
    degreeType = StringField('Degree Type', validators=[DataRequired(), Length(max=50)])
    institution = StringField('Institution', validators=[DataRequired(), Length(max=100)])
    major = StringField('Major', validators=[DataRequired(), Length(max=100)])
    conferredDate = DateField('Conferred Date', format='%Y-%m-%d', validators=[DataRequired()])
    primaryYN = SelectField('Primary?', choices=[('Y', 'Yes'), ('N', 'No')], validators=[DataRequired()])
    submit = SubmitField('Save')

