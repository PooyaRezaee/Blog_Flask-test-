from flask import Blueprint

user = Blueprint('users',__name__,url_prefix='/users/')


from .models import User

# =========== VIEWS ===========
from .views import *