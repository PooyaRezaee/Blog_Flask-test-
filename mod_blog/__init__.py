from flask import Blueprint

blog = Blueprint("blog",__name__,url_prefix="/blog/")

from . import models
from .views import *