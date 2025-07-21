from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class DonationForm(FlaskForm):
    alumniID = IntegerField('Alumni ID', validators=[DataRequired()])
    donationAmt = DecimalField('Amount', validators=[DataRequired()])
    donationDT = DateField('Donation Date', format='%Y-%m-%d', validators=[DataRequired()])
    reason = StringField('Reason')
    description = StringField('Description')
    recurringYN = SelectField('Recurring?', choices=[('Y', 'Yes'), ('N', 'No')], validators=[DataRequired()])
    submit = SubmitField('Save')
