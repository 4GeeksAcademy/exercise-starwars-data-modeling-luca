import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Tabla de usuarios
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    address = Column(String(200), nullable=True)
    phone = Column(String(20), nullable=True)
    favorites = relationship('Favorite', backref='user')

# Tabla de personajes
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    height = Column(String(10), nullable=True)
    mass = Column(String(10), nullable=True)
    hair_color = Column(String(50), nullable=True)
    skin_color = Column(String(50), nullable=True)
    eye_color = Column(String(50), nullable=True)
    birth_year = Column(String(20), nullable=True)
    gender = Column(String(20), nullable=True)
    homeworld = Column(String(100), nullable=True)
    species = Column(String(100), nullable=True)
    films = Column(JSON, nullable=True)
    vehicles = Column(JSON, nullable=True)
    starships = Column(JSON, nullable=True)
    favorites = relationship('Favorite', backref='character')

# Tabla de planetas
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    rotation_period = Column(String(10), nullable=True)
    orbital_period = Column(String(10), nullable=True)
    diameter = Column(String(20), nullable=True)
    climate = Column(String(100), nullable=True)
    gravity = Column(String(50), nullable=True)
    terrain = Column(String(100), nullable=True)
    surface_water = Column(String(50), nullable=True)
    population = Column(String(50), nullable=True)
    favorites = relationship('Favorite', backref='planet')

# Tabla de favoritos
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
