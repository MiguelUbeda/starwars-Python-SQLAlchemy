import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250))
    email = Column(String(250))
    nickname = Column(String(250))
    password = Column(String(250))
    

class Favoritos(Base):
    __tablename__ = 'favoritos' 
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    personaje_id = Column(Integer, ForeignKey('personajes.id'))
    planeta_id = Column(Integer, ForeignKey('planetas.id'))
    planetas = relationship("Planetas")  
    
class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250))
    planet = Column(String(250))
    age = Column(Integer)

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')