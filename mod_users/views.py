from flask import request,render_template,flash,session,redirect,url_for
from . import user
from .forms import Registerform,Loginform
from .models import User
from app import db,Home
from sqlalchemy.exc import IntegrityError
from .utils import add_to_redis,send_singup_message,get_token_redis,delete_token_redis

@user.route("/")
def index():
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

                try:
                    db.session.add(new_user)
                    db.session.commit()
                    flash("Created Your Account")
                    token = add_to_redis(new_user,'register')
                    send_singup_message(new_user,token)
                except IntegrityError:
                    db.session.rollback()
                    flash("Has a error")
                
                return render_template("users/register.html",register_form=register_form)
            else:
                register_form.password_confirm.errors.append("Password Not Match")
                return render_template("users/register.html",register_form=register_form)
        else:
            return render_template("users/register.html",register_form=register_form)

@user.route("/confirm")
def confirm_email():
    email = request.args.get('email')
    token = request.args.get('token')

    user = User.query.filter(User.email.ilike('email')).first()

    if not user:
        flash('email is wrong')
        return redirect(url_for('user.index'))

    if user.active:
        flash('You actived before')
        return redirect(url_for('user.index'))
    
    token_redis = get_token_redis(user,'register')
    
    if not token_redis:
        flash('Wrong/Expired Token')
        return redirect(url_for('user.index'))

    if token != token_redis.decode():
        flash('Wrong/Expired Token')
        return redirect(url_for('user.index'))


    user.active = True
    db.session.commit()
    delete_token_redis(user,'register')

    flash('your account activaty')
    return redirect(url_for('user.index'))