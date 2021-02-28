from . import admin
from flask import session

@admin.route("/")
def admin_index():
    return "welcom to panel admin"

@admin.route("/login/")
def login():
    session['name'] = "pooya"

    return "login page"