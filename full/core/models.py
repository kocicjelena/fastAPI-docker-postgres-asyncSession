import uuid as uuid_pkg
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship
#from .db import Base
Base = declarative_base()
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    todos = relationship("Todos", back_populates="owner")

class Todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("Users", back_populates="todos")

class HealthCheck(BaseModel):
    name: str
    version: str
    description: str


class StatusMessage(BaseModel):
    status: bool
    message: str


