class Natureza:
    
    def __init__(self, codigo_natureza, descricao) -> None:
        self.codigo_natureza = codigo_natureza
        self.descricao = descricao
    
    def json(self):
        return {
                "codigo_natureza": self.codigo_natureza,
                "descricao": self.descricao
               }
