#!/usr/bin/python3
""" class definition of a State """


import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ class state with attrebutes :
    id : aua string with maximum 128 characters and can’t be nullto-generated, unique integer, can’t be null and is a primary key
    name : a string with maximum 128 characters and can’t be null
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name =  Column(String(128), nullable=False)