from flask_wtf import Form
from wtforms import StringField, RadioField, IntegerField, TextAreaField, SelectField, SubmitField
from wtforms import validators


class ContactForm(Form):
    name = StringField("Name", [validators.DataRequired("You must fill your name")])
    gender = RadioField("Gender", choices=[('M', 'Male'), ('F', 'Female')])
    age = IntegerField("Age")
    email = StringField("Email", [validators.DataRequired("Please enter valid email"),
                                  validators.Email('You must fill valid email')])
    message = TextAreaField("Message")
    language = SelectField('Preferred language', choices=[('en', 'English'), ('es', 'Spanish'), ('fr', 'French')])
    submit = SubmitField("Submit")
