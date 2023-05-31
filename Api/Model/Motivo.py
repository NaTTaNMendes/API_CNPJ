class Motivo:

    def __init__(self, codigo_motivo, nome) -> None:
        self.codigo_motivo = codigo_motivo
        self.nome = nome
    
    def json(self):
        return {
                "codigo_motivo": self.codigo_motivo,
                "nome": self.nome
               }   