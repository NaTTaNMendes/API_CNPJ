from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Natureza(Base):
    __tablename__ = 'natureza'
    
    codigo_natureza = Column(Integer, primary_key=True)
    descricao = Column(String(200))
    
    def __init__(self, codigo_natureza, descricao):
        self.codigo_natureza = codigo_natureza
        self.descricao = descricao
    
    def json(self):
        return {
            "codigo_natureza": self.codigo_natureza,
            "descricao": self.descricao
        }