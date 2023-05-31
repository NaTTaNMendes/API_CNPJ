class Empresa:

    def __init__(self, cnpj_base, razao_social, capital_social, porte_empresa, ente_federativo, qualificacao_responsavel, natureza, estabelecimentos, socios) -> None:
        self.cnpj_base = cnpj_base
        self.razao_social = razao_social
        self.capital_social = capital_social
        self.porte_empresa = porte_empresa
        self.ente_federativo = ente_federativo
        self.qualificacao_responsavel = qualificacao_responsavel
        self.natureza = natureza
        self.estabelecimentos = estabelecimentos
        self.socios = socios

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