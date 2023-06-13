from flask import Flask
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from ModelORM.Empresa import Empresa
from ModelORM.Natureza import Natureza
from ModelORM.Pais import Pais
from ModelORM.QualificacaoSocio import QualificacaoSocio
from ModelORM.Socio import Socio

app = Flask(__name__)

engine = create_engine('mysql+mysqlconnector://user:password@host/database')

@app.route('/<path:text>', methods=['GET'])
def read_url_data(text):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    empresa = session.query(Empresa).filter(Empresa.cnpj_base==text[0:8]).first()
    '''
    qualificacao_responsavel = session.query(QualificacaoSocio).get(empresa.codigo_qualificacao_responsavel)
    natureza = session.query(Natureza).get(empresa.codigo_natureza)

    empresa.qualificacao_responsavel = qualificacao_responsavel
    empresa.natureza = natureza
        
    socios_empresa = []
    for socio in session.query(Socio).filter(Socio.cnpj_base==text[0:8]).first():
        pais_socio = session.query(Pais).get(socio.codigo_pais)
        qualificacao_socio = session.query(QualificacaoSocio).get(socio.codigo_qualificacao)
        qualificacao_representante = session.query(QualificacaoSocio).get(socio.qualificacao_representante)
        socio.codigo_pais = pais_socio
        socio.codigo_qualificacao = qualificacao_socio
        socio.qualificacao_representante = qualificacao_representante
        socios_empresa.append(socio)
    
    empresa.socios = socios_empresa
    '''
    return empresa.json()

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', debug=False)