#!/usr/bin/python3
'''
    a script that contains calss definition of state
    and an instance Base = declarative_base()
'''
from sqlalchemy import Column, Integer, String, UniqueConstraint, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
