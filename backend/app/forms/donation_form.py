from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class DonationForm(FlaskForm):
    alumniID = IntegerField('Alumni ID', validators=[DataRequired()])
    amount = DecimalField('Amount', places=2, validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d')
    reason = StringField('Reason', validators=[Length(max=100)])
    description = StringField('Description', validators=[Length(max=255)])
    submit = SubmitField('Save')
