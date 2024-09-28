from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo


class Registration_Form(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=4, max=15)])
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired(), EqualTo('repeat_password')])
    repeat_password = PasswordField(validators=[DataRequired()])
    country = SelectField(validators=[DataRequired()], choices=['USA', 'Germany', 'Brazil', 'Japan', 'Indian', 'Other'])
    position = SelectField(validators=[DataRequired()], choices=['Software Enginneer', 'WebDeveloper', 'AppDeveloper', 'Software Developer', 'Data Scientist', 'DevOps Engineer', 'Game Developer', 'Artificial Intelligence Programmer', 'Software Architect'])
    short_biography = TextAreaField(validators=[DataRequired()])
    
class Login_Form(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])