from sqlalchemy import Column,Integer,String
from app import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = 'USERS'

    Id = db.Column(Integer(),primary_key=True)
    full_name = db.Column(String(128),nullable=True)
    Age = db.Column(Integer(),nullable=True)
    Email = db.Column(String(128),nullable=False,unique=True)
    password = db.Column(String(1280),nullable=False)
    rol = db.Column(String(128),nullable=False)


    def set_password(self,password):
        self.password = generate_password_hash(password)
