class Estabelecimento:

    def __init__(self, cnpj_base,
                 cnpj_ordem,
                 cnpj_dv,
                 identificador_matriz,
                 nome_fantasia,
                 situacao_cadastral,
                 data_situacao_cadastral,
                 nome_cidade_exterior,
                 inicio_atividade,
                 tipo_logradouro,
                 logradouro,
                 numero,
                 complemento,
                 bairro,
                 cep,
                 uf,
                 ddd1,
                 telefone1,
                 ddd2,
                 telefone2,
                 ddd_fax,
                 fax,
                 email,
                 situacao_especial,
                 data_situacao_especial,
                 cnae_principal,
                 cnaes_secundarios,
                 motivo,
                 municipio,
                 pais) -> None:
        self.cnpj_base = cnpj_base
        self.cnpj_ordem = cnpj_ordem
        self.cnpj_dv = cnpj_dv
        self.identificador_matriz = identificador_matriz
        self.nome_fantasia = nome_fantasia
        self.situacao_cadastral = situacao_cadastral
        self.data_situacao_cadastral = data_situacao_cadastral
        self.nome_cidade_exterior = nome_cidade_exterior
        self.inicio_atividade = inicio_atividade
        self.tipo_logradouro = tipo_logradouro
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cep = cep
        self.uf = uf
        self.ddd1 = ddd1
        self.telefone1 = telefone1
        self.ddd2 = ddd2
        self.telefone2 = telefone2
        self.ddd_fax = ddd_fax
        self.fax = fax
        self.email = email
        self.situacao_especial = situacao_especial
        self.data_situacao_especial = data_situacao_especial
        self.cnae_principal = cnae_principal
        self.cnaes_secundarios = cnaes_secundarios
        self.motivo = motivo
        self.municipio = municipio
        self.pais = pais
    
    def json(self):
        cnaes_secundarios_json = [cnae.json() for cnae in self.cnaes_secundarios] if self.cnaes_secundarios is not None else None
        cnae_principal_json = self.cnae_principal.json() if self.cnae_principal is not None else None
        motivo_json = self.motivo.json() if self.motivo is not None else None
        municipio_json = self.municipio.json() if self.municipio is not None else None
        pais_json = self.pais.json() if self.pais is not None else None

        return {
                "cnpj_base": self.cnpj_base,
                "cnpj_ordem": self.cnpj_ordem,
                "cnpj_dv": self.cnpj_dv,
                "identificador_matriz": self.identificador_matriz,
                "nome_fantasia": self.nome_fantasia,
                "situacao_cadastral": self.situacao_cadastral,
                "data_situacao_cadastral": self.data_situacao_cadastral.strftime("%d/%m/%Y"),
                "nome_cidade_exterior": self.nome_cidade_exterior,
                "inicio_atividade": self.inicio_atividade.strftime("%d/%m/%Y"),
                "tipo_logradouro": self.tipo_logradouro,
                "logradouro": self.logradouro,
                "numero": self.numero,
                "complemento": self.complemento,
                "bairro": self.bairro,
                "cep": self.cep,
                "uf": self.uf,
                "ddd1": self.ddd1,
                "telefone1": self.telefone1,
                "ddd2": self.ddd2,
                "telefone2": self.telefone2,
                "ddd_fax": self.ddd_fax,
                "fax": self.fax,
                "email": self.email,
                "situacao_especial": self.situacao_especial,
                "data_situacao_especial" : self.data_situacao_especial.strftime("%d/%m/%Y"),
                "cnae_principal": cnae_principal_json,
                "cnaes_secundarios": cnaes_secundarios_json,
                "motivo": motivo_json,
                "municipio": municipio_json,
                "pais": pais_json
               }