from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from config import Development
from flask_migrate import Migrate
from flask_mail import Mail
from redis import Redis

app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
mail = Mail(app)
redis = Redis.from_url(app.config['REDIS_SERVER_URL'])

# =========== VIEWS ===========
from views import Home

# =========== BluePrints ===========
from mod_users import user
from mod_admin import admin
from mod_blog import blog
from mod_uploads import uploads

app.register_blueprint(admin)
app.register_blueprint(user)
app.register_blueprint(blog)
app.register_blueprint(uploads)