from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Municipio(Base):
    __tablename__ = 'municipio'
    
    codigo_municipio = Column(Integer, primary_key=True)
    nome = Column(String(200))
    
    def __init__(self, codigo_municipio, nome):
        self.codigo_municipio = codigo_municipio
        self.nome = nome
    
    def json(self):
        return {
            "codigo_municipio": self.codigo_municipio,
            "nome": self.nome
        }