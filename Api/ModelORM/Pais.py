from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pais(Base):
    __tablename__ = 'pais'
    
    codigo_pais = Column(Integer, primary_key=True)
    nome = Column(String(100))
    
    def __init__(self, codigo_pais, nome):
        self.codigo_pais = codigo_pais
        self.nome = nome
    
    def json(self):
        return {
            "codigo_pais": self.codigo_pais,
            "nome": self.nome
        }