from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class SkillsetForm(FlaskForm):
    alumniID = IntegerField('Alumni ID', validators=[DataRequired()])
    skillName = StringField('Skill Name', validators=[DataRequired(), Length(max=50)])
    proficiencyLevel = SelectField('Proficiency', choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ], validators=[DataRequired()])
    submit = SubmitField('Save')


