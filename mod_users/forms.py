from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField,IntegerField
from wtforms import PasswordField,StringField
from wtforms.validators import DataRequired

class Loginform(FlaskForm):
    email = EmailField(validators=[DataRequired()],render_kw={"placeholder":"Email"})
    password = PasswordField(validators=[DataRequired()],render_kw={"placeholder":"Passwrd"})

class Registerform(FlaskForm):
    full_name = StringField(validators=[DataRequired()],render_kw={"placeholder":"Full Name"})
    age = IntegerField(render_kw={"placeholder":"Age"})
    email = EmailField(validators=[DataRequired()],render_kw={"placeholder":"Email"})
    password = PasswordField(validators=[DataRequired()],render_kw={"placeholder":"Passwrd"})
    password_confirm = PasswordField(validators=[DataRequired()],render_kw={"placeholder":"Re-Password"})