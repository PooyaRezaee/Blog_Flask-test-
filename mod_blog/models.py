from app import db
from sqlalchemy import Column,Integer,String,Text

class Category(db.Model):
    __tablename__ = 'category'
    Id = Column(Integer,primary_key=True)
    name = Column(String(128),nullable=False,unique=True)
    description = Column(String(256),nullable=False)
    slug = Column(String(128),nullable=False,unique=True)

class post(db.Model):
    __tablename__ = 'post'
    Id = Column(Integer,primary_key=True)
    title = Column(String(128),nullable=False,unique=True)
    summary = Column(String(256),nullable=False)
    content = Column(Text,nullable=False)
    slug = Column(String(128),nullable=False,unique=True)