from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class SkillsetForm(FlaskForm):
    skillName = StringField('Skill Name', validators=[DataRequired(), Length(max=100)])
    proficiencyLevel = StringField('Proficiency Level', validators=[Length(max=50)])
    endorsementYN = SelectField('Endorsed?', choices=[('Y', 'Yes'), ('N', 'No')])
    dateReceived = DateField('Date Received', format='%Y-%m-%d')
    submit = SubmitField('Save')

