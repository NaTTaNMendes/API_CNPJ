class Municipio:

    def __init__(self, codigo_municipio, nome) -> None:
        self.codigo_municipio = codigo_municipio
        self.nome = nome
    
    def json(self):
        return {
                "codigo_municipio": self.codigo_municipio,
                "nome": self.nome 
               }       