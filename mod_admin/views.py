from . import admin
from flask import session,render_template,request,abort,flash
from mod_users.forms import Loginform
from mod_users.models import User

@admin.route("/")
def admin_index():
    if session.get('rol') == "admin":
        return "welcom to panel admin"
    else:
        abort(404)

@admin.route("/login/",methods=["GET","POST"])
def login():
    # session['name'] = "pooya"
    login_form = Loginform(request.form)

    if request.method == "POST":
        if not login_form.validate_on_submit():
            abort(400)
        user = User.query.filter(User.Email.ilike(f"{login_form.email.data}")).first()
        if not user:
            flash("Email is Wrong",category="error")
            return render_template("admin/login.html",login_form=login_form) 
        if not user.check_password(login_form.password.data):
            flash("Passowrd is Wrong",category="error")
            return render_template("admin/login.html",login_form=login_form)
        if not user.is_admin():
            flash("You not admin",category="error")
            return render_template("admin/login.html",login_form=login_form)
        session["email"] = user.Email
        session["id"] = user.Id
        session["rol"] = user.rol
        return "Congratolation , You are logged"
    
    if session.get('rol') == "admin":
        return "Are Logged from before !!!"

    return render_template("admin/login.html",login_form=login_form)