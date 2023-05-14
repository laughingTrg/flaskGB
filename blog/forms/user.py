from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField

class UserBaseForm(FlaskForm):
    first_name = StringField('First name')
    last_name = StringField('Last name')
    email = StringField('E-mail', [validators.DataRequired(), validators.Email()], filters=[lambda data: data and data.lower()],)

class UserRegisterForm(UserBaseForm):
    password = PasswordField("New password", [validators.DataRequired(), validators.EqualTo('pass_confirm', message='Passwords must match')])
    pass_confirm = PasswordField("Repeat password")
    submit = SubmitField('Register')

class UserLoginForm(FlaskForm):
    email = StringField('E-mail', [validators.DataRequired(), validators.Email()], filters=[lambda data: data and data.lower()],)
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')
