#!/usr/bin/python3
"""
Define class State
Use of sqlalchemy to link to the MySQL db
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class tor reresent the states table defined
    __tablename__(str): name of the sql table to store class States
    id (Integer): the state's id
    name (String): the state's name
    """
    __tablename__ = "states"
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True,
        autoincrement=True
    )
    name = Column(String(128), nullable=False)
