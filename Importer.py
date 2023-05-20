from Connection import Connection
from Commands import Commands

def main():
    connection = Connection('localhost', 'api_cnpj', 'root', '17102003naruto')
    commands = Commands(connection)

    connection.connect()

    commands.loadCnae(r'Data/cnaes.csv')
    commands.loadNaturezaJuridica(r'Data/naturezas.csv')
    commands.loadPais(r'Data/paises.csv')
    commands.loadQualificacaoSocio(r'Data/qualificacoes.csv')

    connection.disconnect()

if __name__ == '__main__':
    main()