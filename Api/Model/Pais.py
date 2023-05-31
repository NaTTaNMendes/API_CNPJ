class Pais:

    def __init__(self, codigo_pais, nome) -> None:
        self.codigo_pais = codigo_pais
        self.nome = nome
    
    def json(self):
        return {
                "codigo_pais": self.codigo_pais,
                "nome": self.nome
               }