from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

import full.core.db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("StaffBase", back_populates="todos")



class StaffBase(Base):
    __tablename__ = "staff"
    id = Column(Integer, primary_key=True, index=True)
   
    nickname: str = Column(Integer, primary_key=True, index=True)
    todos = relationship("Todos", back_populates="owner")






