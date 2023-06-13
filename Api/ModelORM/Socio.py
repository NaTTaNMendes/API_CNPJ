from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Socio(Base):
    __tablename__ = 'socio'
    
    socio_id = Column(Integer, primary_key=True)
    cnpj_base = Column(Integer)
    identificador = Column(Integer)
    nome = Column(String(200))
    cnpj_cpf_socio = Column(Integer)
    entrada_sociedade = Column(Date)
    representante_cpf = Column(Integer)
    nome_representante = Column(String(150))
    faixa_etaria = Column(Integer)    
    codigo_pais = Column(Integer, ForeignKey('codigo_pais'))
    codigo_qualificacao = Column(Integer, ForeignKey('codigo_qualificacao'))   
    qualificacao_representante = Column(Integer, ForeignKey('qualificacao_representante'))
    
    def __init__(self, id_socio, cnpj_base, identificador, nome, cnpj_cpf_socio, entrada_sociedade, codigo_pais, representante_cpf,
                 nome_representante, qualificacao_representante, faixa_etaria, qualificacao):
        self.id = id_socio
        self.cnpj_base = cnpj_base
        self.identificador = identificador
        self.nome = nome
        self.cnpj_cpf_socio = cnpj_cpf_socio
        self.entrada_sociedade = entrada_sociedade
        self.codigo_pais = codigo_pais
        self.representante_cpf = representante_cpf
        self.nome_representante = nome_representante
        self.qualificacao_representante = qualificacao_representante
        self.faixa_etaria = faixa_etaria
        self.codigo_qualificacao = qualificacao
    
    def json(self):
        pais_json = self.codigo_pais.json() if self.codigo_pais is not None else None
        qualificacao_json = self.codigo_qualificacao.json() if self.codigo_qualificacao is not None else None
        qualificacao_representante_json = self.qualificacao_representante.json() if self.qualificacao_representante is not None else None

        return {
            "id_socio": self.id,
            "cnpj_base": self.cnpj_base,
            "identificador": self.identificador,
            "nome": self.nome,
            "cnpj_cpf_socio": self.cnpj_cpf_socio,
            "entrada_sociedade": self.entrada_sociedade.strftime("%d/%m/%Y"),
            "pais": pais_json,
            "representante_cpf": self.representante_cpf,
            "nome_representante": self.nome_representante,
            "qualificacao_representante": qualificacao_representante_json,
            "faixa_etaria": self.faixa_etaria,
            "qualificacao": qualificacao_json
        }