from sqlalchemy import Column,Integer,String,Boolean
from app import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    Id = db.Column(Integer(),primary_key=True)
    full_name = db.Column(String(128),nullable=True)
    Age = db.Column(Integer(),nullable=True)
    Email = db.Column(String(128),nullable=False,unique=True)
    password = db.Column(String(1280),nullable=False)
    rol = db.Column(String(128),nullable=False)
    active = db.Column(Boolean(),nullable=False,default=False)


    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

    def is_admin(self):
        if self.rol == "admin":
            return True
        if self.rol == "user":
            return False
