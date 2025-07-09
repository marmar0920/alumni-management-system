from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class NewsletterForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired(), Length(max=150)])
    body = TextAreaField('Body', validators=[DataRequired()])
    sendDate = DateField('Send Date', format='%Y-%m-%d')
    submit = SubmitField('Save')

