from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Motivo(Base):
    __tablename__ = 'motivo'
    
    codigo_motivo = Column(Integer, primary_key=True)
    nome = Column(String(200))
    
    def __init__(self, codigo_motivo, nome):
        self.codigo_motivo = codigo_motivo
        self.nome = nome
    
    def json(self):
        return {
            "codigo_motivo": self.codigo_motivo,
            "nome": self.nome
        }