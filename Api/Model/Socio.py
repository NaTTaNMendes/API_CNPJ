import datetime

class Socio:

    def __init__(self, id_socio,
                 cnpj_base,
                 identificador,
                 nome,
                 cnpj_cpf_socio,
                 entrada_sociedade,
                 pais,
                 representante_cpf,
                 nome_representante,
                 qualificacao_representante,
                 faixa_etaria,
                 qualificacao) -> None:
        self.id = id_socio
        self.cnpj_base = cnpj_base
        self.identificador = identificador
        self.nome = nome
        self.cnpj_cpf_socio = cnpj_cpf_socio
        self.entrada_sociedade = entrada_sociedade
        self.pais = pais
        self.representante_cpf = representante_cpf
        self.nome_representante = nome_representante
        self.qualificacao_representante = qualificacao_representante
        self.faixa_etaria = faixa_etaria
        self.qualificacao = qualificacao
    
    def json(self):
        pais_json = self.pais.json() if self.pais is not None else None
        qualificacao_json = self.qualificacao.json() if self.qualificacao is not None else None
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
