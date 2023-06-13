from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class QualificacaoSocio(Base):
    __tablename__ = 'qualificacao_socio'
    
    codigo_qualificacao = Column(Integer, primary_key=True)
    descricao = Column(String(100))
    
    def __init__(self, codigo_qualificacao, descricao):
        self.codigo_qualificacao = codigo_qualificacao
        self.descricao = descricao
    
    def json(self):
        return {
            "codigo_qualificacao": self.codigo_qualificacao,
            "descricao": self.descricao
        }