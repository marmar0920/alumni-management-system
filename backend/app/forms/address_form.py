from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class AddressForm(FlaskForm):
    address = StringField(
        'Street Address',
        validators=[
            DataRequired(),
            Length(max=100, message='Street Address cannot exceed 100 characters')
        ]
    )
    city = StringField(
        'City',
        validators=[
            DataRequired(),
            Length(max=50, message='City cannot exceed 50 characters')
        ]
    )
    state = StringField(
        'State',
        validators=[
            DataRequired(),
            Length(min=2, max=2, message='State must be exactly 2 characters')
        ]
    )
    zipCode = StringField(
        'Zip Code',
        validators=[
            DataRequired(),
            Length(max=10, message='Zip Code cannot exceed 10 characters')
        ]
    )
    activeYN = SelectField(
        'Active?',
        choices=[('Y', 'Yes'), ('N', 'No')],
        validators=[DataRequired()]
    )
    primaryYN = SelectField(
        'Primary?',
        choices=[('Y', 'Yes'), ('N', 'No')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Save')
