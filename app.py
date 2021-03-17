from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from config import Development
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

# =========== VIEWS ===========
from views import Home

# =========== BluePrints ===========
from mod_users import user
from mod_admin import admin
from mod_blog import blog

app.register_blueprint(admin)
app.register_blueprint(user)
app.register_blueprint(blog)