from flask import Blueprint


admin = Blueprint('admin',__name__,url_prefix='/admin/')



# =========== VIEWS ===========
from .views import index
from .views import login
from .views import log_out