from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, SelectField, StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class DonationForm(FlaskForm):
    alumniID = IntegerField('Alumni ID', validators=[DataRequired()])
    donationAmt = DecimalField('Amount', places=2, validators=[DataRequired()])
    donationDT = DateField('Date', format='%Y-%m-%d')
    reason = StringField('Reason', validators=[Length(max=100)])
    description = StringField('Description', validators=[Length(max=255)])
    submit = SubmitField('Save')
