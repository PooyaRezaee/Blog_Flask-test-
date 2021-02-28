from flask import Blueprint

user = Blueprint('users',__name__,url_prefix='/users/')


from .models import User

@user.route("/")
def users_index():
    return "welcom to panel users"
    