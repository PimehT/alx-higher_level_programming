#!/usr/bin/python3
"""
Define class City
Use of sqlalchemy to link to the MySQL db
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    City class tor reresent the cities table defined
    __tablename__(str): name of the sql table to store class City
    id (Integer): the city's id
    name (String): the city's name
    state_id (Integer): the foreign key from state id
    """
    __tablename__ = "cities"
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True,
        autoincrement=True
    )
    name = Column(
        String(128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )
