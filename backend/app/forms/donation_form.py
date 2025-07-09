from flask_wtf import FlaskForm
from wtforms import DateField, DecimalField, StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class DonationForm(FlaskForm):
    donationDate = DateField('Donation Date', format='%Y-%m-%d', validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[DataRequired()])
    method = StringField('Method', validators=[DataRequired()])
    recurringYN = SelectField('Recurring?', choices=[('Y', 'Yes'), ('N', 'No')], validators=[DataRequired()])
    notes = TextAreaField('Notes')
    submit = SubmitField('Save')

