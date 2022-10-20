#!/usr/bin/python3
'''
    a script that contains calss definition of state
    and an instance Base = declarative_base()
'''
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class City(Base):
    '''city class that creates cities table'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),nullable=False)
