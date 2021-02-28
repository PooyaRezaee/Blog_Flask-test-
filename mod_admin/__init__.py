from flask import Blueprint


admin = Blueprint('admin',__name__,url_prefix='/admin/')



# =========== VIEWS ===========
from .views import admin_index