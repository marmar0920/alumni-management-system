from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired, Length

class SkillsetForm(FlaskForm):
    alumniID = IntegerField('Alumni ID', validators=[DataRequired()])
    skill = StringField('Skill Name', validators=[DataRequired(), Length(max=50)])
    description = StringField('Description', validators=[DataRequired(), Length(max=500)])
    proficiency = SelectField('Proficiency', choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ], validators=[DataRequired()])
    submit = SubmitField('Save')
