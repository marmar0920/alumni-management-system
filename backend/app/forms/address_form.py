from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class AddressForm(FlaskForm):
    address = StringField('Street Address', validators=[DataRequired(), Length(max=50)])
    city = StringField('City', validators=[DataRequired(), Length(max=50)])
    state = StringField('State', validators=[DataRequired(), Length(min=2, max=2)])
    zipCode = StringField('Zip Code', validators=[DataRequired(), Length(max=10)])
    activeYN = SelectField('Active?', choices=[('Y', 'Yes'), ('N', 'No')], validators=[DataRequired()])
    primaryYN = SelectField('Primary?', choices=[('Y', 'Yes'), ('N', 'No')], validators=[DataRequired()])
    submit = SubmitField('Save')
