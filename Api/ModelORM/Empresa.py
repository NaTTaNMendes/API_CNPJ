from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from ModelORM.Natureza import Natureza

from ModelORM.QualificacaoSocio import QualificacaoSocio

Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresa'

    cnpj_base = Column(String, primary_key=True)
    razao_social = Column(String(300))
    capital_social = Column(Float)
    porte_empresa = Column(Integer)
    ente_federativo = Column(String(100))
    #codigo_qualificacao_responsavel = Column(Integer, ForeignKey('qualificacao_responsavel'))
    #codigo_natureza = Column(Integer, ForeignKey('codigo_natureza'))
    estabelecimentos = None
    socios = []
    qualificacao_responsavel = None
    natureza = None

    def json(self):
        estabelecimentos_json = [estabelecimento.json() for estabelecimento in self.estabelecimentos] if self.estabelecimentos else None
        socios_json = [socio.json() for socio in self.socios] if self.socios else None
        porte = self.porte_empresa
        natureza_json = self.natureza.json() if self.natureza else None
        qualificacao_json = self.qualificacao_responsavel.json() if self.qualificacao_responsavel else None

        return {
            "cnpj_base": self.cnpj_base,
            "razao_social": self.razao_social,
            "capital_social": self.capital_social,
            "porte_empresa": str(porte).split('.')[-1],
            "ente_federativo": self.ente_federativo,
            "qualificacao_responsavel": qualificacao_json,
            "natureza": natureza_json,
            "estabelecimentos": estabelecimentos_json,
            "socios": socios_json
        }