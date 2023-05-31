class QualificacaoSocio:
    
    def __init__(self, codigo_qualificacao, descricao) -> None:
        self.codigo_qualificacao = codigo_qualificacao
        self.descricao = descricao
    
    def json(self):
        return {
                "codigo_qualificacao": self.codigo_qualificacao,
                "descricao": self.descricao
               }