import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    

class characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    characters_name= Column(String(250))
    gender = Column(String(250))
    skills = Column(String(250))
    height = Column(String(250))
    species = Column(String(250))

class favorite_characters(Base):
    __tablename__ = 'favorite_characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))

class planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    population = Column(String(250))
    gravity = Column(String(250))
    climate = Column(String(250))
    composition = Column(String(250))

class favorite_planets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))

class vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    vehicles_name = Column(String(250))
    size = Column(String(250))
    speed = Column(String(250))
    fuel = Column(String(250))

class favorite_vehicles(Base):
    __tablename__ = 'favorite_vehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')