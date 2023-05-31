class Cnae:

    def __init__(self, codigo_cnae, descricao) -> None:
        self.codigo_cnae = codigo_cnae
        self.descricao = descricao
    
    def json(self):
        return {
                "codigo_cnae": self.codigo_cnae,
                "descricao": self.descricao
               }