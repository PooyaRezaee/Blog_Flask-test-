from . import admin
from flask import session,render_template,request,abort,flash
from mod_users.forms import Loginform
from mod_users.models import User

@admin.route("/")
def admin_index():
    return "welcom to panel admin"

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
            
        session["email"] = user.Email
        session["id"] = user.Id
        return "Congratolation , You are logged"
    
    if session.get('email') is not None:
        return "Are Logged from before !!!"

    return render_template("admin/login.html",login_form=login_form)