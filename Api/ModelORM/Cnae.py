from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Cnae(Base):
    __tablename__ = 'cnae'
    codigo_cnae = Column(Integer, primary_key=True)
    descricao = Column(String(170))

    def json(self):
        return {
                "codigo_cnae": self.codigo_cnae,
                "descricao": self.descricao
               }
