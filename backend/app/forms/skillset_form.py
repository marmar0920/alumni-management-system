from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired, Length

class SkillsetForm(FlaskForm):
    alumniID = IntegerField('Alumni ID', validators=[DataRequired()])
    skillName = StringField('Skill Name', validators=[DataRequired(), Length(max=50)])
    proficiencyLevel = SelectField('Proficiency', choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ], validators=[DataRequired()])
    endorsementYN = SelectField('Endorsed?', choices=[
        ('Y', 'Yes'),
        ('N', 'No')
    ], validators=[DataRequired()])
    dateReceived = DateField('Date Received', format='%Y-%m-%d')
    submit = SubmitField('Save')
