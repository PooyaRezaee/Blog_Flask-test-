from . import admin
from flask import session,render_template,request
from mod_users.forms import Loginform

@admin.route("/")
def admin_index():
    return "welcom to panel admin"

@admin.route("/login/")
def login():
    # session['name'] = "pooya"
    login_form = Loginform(request.form)

    return render_template("admin/index.html",login_form=login_form)