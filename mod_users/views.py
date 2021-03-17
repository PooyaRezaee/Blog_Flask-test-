from flask import request,render_template,flash,session
from . import user
from .forms import Registerform,Loginform
from .models import User
from app import db,Home

@user.route("/")
def users_index():
    return "welcom to panel users"

@user.route("/register",methods=["GET","POST"])
def Register():
    register_form = Registerform(request.form)

    if request.method == "GET":
        return render_template("users/register.html",register_form=register_form)
    elif request.method == "POST":
        if register_form.validate_on_submit():
            if register_form.password.data == register_form.password_confirm.data:
                new_user = User()
                new_user.full_name = register_form.full_name.data
                new_user.Age = register_form.age.data
                new_user.Email = register_form.email.data
                new_user.set_password(register_form.password.data)
                new_user.rol = "user"

                old_user_email = User.query.filter(User.Email.ilike(new_user.Email)).first()
                if old_user_email:
                    flash("Email was Register in site","error")
                    return render_template("users/register.html",register_form=register_form)

                db.session.add(new_user)
                db.session.commit()
                # db.session.rollback() for clear session
                flash("Created Your Account")
                
                return render_template("users/register.html",register_form=register_form)
            else:
                register_form.password_confirm.errors.append("Password Not Match")
                return render_template("users/register.html",register_form=register_form)
        else:
            return render_template("users/register.html",register_form=register_form)