from decimal import Decimal
import json
from flask import Response, jsonify, make_response
from Model.Cnae import Cnae
from Model.Empresa import Empresa
from Model.Enums.PorteEmpresa import PorteEmpresa
from Model.Estabelecimento import Estabelecimento
from Model.Motivo import Motivo
from Model.Municipio import Municipio
from Model.Natureza import Natureza
from Model.Pais import Pais
from Model.QualificacaoSocio import QualificacaoSocio
from Model.Socio import Socio
import re

class DecimalEncoder(json.JSONEncoder):
    
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)

class MainHelper:
    
    def __init__(self, connection) -> None:
        self.connection = connection
     
    def carregaEmpresa(self, cnpj):
        itens_empresa = []
        
        query = "SELECT * FROM empresa where (cnpj_base = %s)"
        self.connection.cursor.execute(query, (cnpj[0:8],))
        itens_empresa = self.connection.cursor.fetchall()

        qualificacao = self.__getQualificacaoSocio(itens_empresa[0][3])
        natureza = self.__getNatureza(itens_empresa[0][2])
        socios = self.__getSocios(cnpj)
        estabelecimentos = self.__getEstabelecimentos(cnpj)

        empresa = Empresa(cnpj_base=itens_empresa[0][0],
                          razao_social=itens_empresa[0][1],
                          capital_social=itens_empresa[0][4],
                          porte_empresa=PorteEmpresa(itens_empresa[0][5]),
                          ente_federativo=itens_empresa[0][6],
                          qualificacao_responsavel=qualificacao,
                          natureza=natureza,
                          estabelecimentos=estabelecimentos,
                          socios=socios)

        return empresa

    def __getQualificacaoSocio(self, codigo_qualificacao):
        query = "SELECT descricao FROM qualificacao_socio where (codigo_qualificacao = %s)"
        self.connection.cursor.execute(query, (codigo_qualificacao,))
        result = self.connection.cursor.fetchall()     
        try:
            descricao = result[0][0]
        except:
            descricao = None
        return QualificacaoSocio(codigo_qualificacao, descricao)
    
    def __getNatureza(self, codigo_natureza):
        query = "SELECT descricao FROM natureza where (codigo_natureza = %s)"
        self.connection.cursor.execute(query, (codigo_natureza,))
        result = self.connection.cursor.fetchall()
        try:
            descricao = result[0][0]
        except:
            descricao = None
        return Natureza(codigo_natureza, descricao)
    
    def __getPais(self, codigo_pais):
        query = "SELECT nome FROM pais where (codigo_pais = %s)"
        self.connection.cursor.execute(query, (codigo_pais,))
        result = self.connection.cursor.fetchall()
        try:
            descricao = result[0][0]
        except:
            descricao = None
        return Pais(codigo_pais, descricao)

    def __getMunicipio(self, codigo_municipio):
        query = "SELECT nome FROM municipio where (codigo_municipio = %s)"
        self.connection.cursor.execute(query, (codigo_municipio,))
        item_municipio = self.connection.cursor.fetchall()
        try:
            nome = item_municipio[0][0]
        except:
            nome = None
        return Municipio(codigo_municipio, nome)

    def __getMotivo(self, codigo_motivo):
        query = "SELECT descricao FROM motivo where (codigo_motivo = %s)"
        self.connection.cursor.execute(query, (codigo_motivo,))
        item_motivo = self.connection.cursor.fetchall()
        try:
            descricao = item_motivo[0][0]
        except:
            descricao = None
        return Motivo(codigo_motivo, descricao)

    def __getCnae(self, codigo_cnae):
        query = "SELECT descricao FROM cnae where (codigo_cnae = %s)"
        self.connection.cursor.execute(query, (codigo_cnae,))
        cnae = self.connection.cursor.fetchall()
        try:
            descricao = cnae[0][0]
        except:
            descricao = None
        return Cnae(codigo_cnae, descricao)

    def __getSocios(self, cnpj):        
        query = "SELECT * FROM socio where (cnpj_base = %s)"
        self.connection.cursor.execute(query, (cnpj[0:8],))
        itens_socio = self.connection.cursor.fetchall()
        socios = []

        for item in itens_socio:
            qualificacao_representante = self.__getQualificacaoSocio(item[10])
            qualificacao = self.__getQualificacaoSocio(item[5])
            pais = self.__getPais(item[7])

            socio = Socio(id_socio=item[0],
                          cnpj_base=item[1],
                          identificador=item[2],
                          nome=item[3],
                          cnpj_cpf_socio=item[4],
                          entrada_sociedade=item[6],
                          pais=pais,
                          representante_cpf=item[8],
                          nome_representante=item[9],
                          qualificacao_representante=qualificacao_representante,
                          faixa_etaria=item[11],
                          qualificacao=qualificacao)
            socios.append(socio)
        
        return socios

    def __getEstabelecimentos(self, cnpj):
        query = "SELECT * FROM estabelecimento where (cnpj_base = %s)"
        self.connection.cursor.execute(query, (cnpj[0:8],))
        itens_estabelecimento = self.connection.cursor.fetchall()
        
        estabelecimentos = []
        for item in itens_estabelecimento:
            motivo = self.__getMotivo(item[7])
            pais = self.__getPais(item[9])
            cnae = self.__getCnae(item[11])
            municipio = self.__getMunicipio(item[19])

            estabelecimento = Estabelecimento(cnpj_base=item[0],
                                            cnpj_ordem=item[1],
                                            cnpj_dv=item[2],
                                            identificador_matriz=item[3],
                                            nome_fantasia=item[4],
                                            situacao_cadastral=item[5],
                                            data_situacao_cadastral=item[6],
                                            nome_cidade_exterior=item[8],
                                            inicio_atividade=item[10],
                                            tipo_logradouro=item[12],
                                            logradouro=item[13],
                                            numero=item[14],
                                            complemento=item[15],
                                            bairro=item[16],
                                            cep=item[17],
                                            uf=item[18],
                                            ddd1=item[20],
                                            telefone1=item[21],
                                            ddd2=item[22],
                                            telefone2=item[23],
                                            ddd_fax=item[24],
                                            fax=item[25],
                                            email=item[26],
                                            situacao_especial=item[27],
                                            data_situacao_especial=item[28],
                                            cnae_principal=cnae,
                                            cnaes_secundarios=None,
                                            motivo=motivo,
                                            municipio=municipio,
                                            pais=pais
                                            )

            estabelecimentos.append(estabelecimento)
        
        return estabelecimentos

    def __contains_only_numbers(self, text):
        pattern = r'^\d{14}$'
        return bool(re.match(pattern, text))
    
    def verificaCnpj(self, cnpj):
        if not self.__contains_only_numbers(cnpj):
            error_message = {'error': 'CNPJ INVALIDO OU FORA DA FORMATACAO'}
            return make_response(jsonify(error_message), 400)
        return None
    
    def retorna(self, empresa):
        response_data = json.dumps(empresa.json(), cls=DecimalEncoder, ensure_ascii=False, indent=4)
        response = Response(response_data, content_type='application/json; charset=utf-8')
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['Content-Security-Policy'] = 'default-src \'self\''
        return response