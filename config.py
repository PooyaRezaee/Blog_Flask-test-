import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    MAIL_SERVER = 'smtp@gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL=True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    REDIS_SERVER_URL = os.getenv("REDIS_SERVER_URL")

class Development(Config):
    DEBUG = True

class Product(Config):
    DEBUG = False
