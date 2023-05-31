from Connection import Connection
from Commands import Commands

def main():
    connection = Connection('localhost', 'api_cnpj', 'root', '17102003naruto')
    commands = Commands(connection)

    connection.connect()

    #commands.loadCnae(r'Data/cnaes.csv')
    #commands.loadNaturezaJuridica(r'Data/naturezas.csv')   
    #ommands.loadPais(r'Data/paises.csv')
    #commands.loadQualificacaoSocio(r'Data/qualificacoes.csv')
    #commands.loadMunicipio(r'Data/municipios.csv')
    #commands.loadSocio(r'Data/socios0.csv')
    #print('TERMINEI O SOCIOS 0')

    #commands.loadSocio(r'Data/socios4.csv', 10660752)
    #print('TERMINEI O SOCIOS 4')
    #commands.loadSocio(r'Data/socios9.csv', 20756497)
    #print('TERMINEI O SOCIOS 9')

    #commands.loadSimples(r'Data/simples.csv')
    #print('Terminei o SIMPLES')

    #commands.loadEmpresas(r'Data/empresas0.csv')
    #print('Terminei o Empresas 0')

    #commands.loadEmpresas(r'Data/empresas1.csv')
    #print('Terminei o Empresas1')

    #commands.loadEmpresas(r'Data/empresas2.csv')
    #print('Terminei o Empresas 2')

    #commands.loadEmpresas(r'Data/empresas3.csv')
    #print('Terminei o Empresas 3')

    #commands.loadEmpresas(r'Data/empresas4.csv')
    #print('Terminei o Empresas 4')

    #commands.loadEmpresas(r'Data/empresas5.csv')
    #print('Terminei o Empresas 5')

    #commands.loadEmpresas(r'Data/empresas6.csv')
    #print('Terminei o Empresas 6')

    #commands.loadEmpresas(r'Data/empresas7.csv')
    #print('Terminei o Empresas 7')

    #commands.loadEmpresas(r'Data/empresas8.csv')
    #print('Terminei o Empresas 8')

    #commands.loadEmpresas(r'Data/empresas9.csv')
    #print('Terminei o Empresas 9')
    
    #commands.loadMotivo(r'Data/motivos.csv')

    commands.loadEstabelecimentos(r'Data/estabelecimentos0.csv')
    print('Terminei o Estabelecimentos 0')

    commands.loadEstabelecimentos(r'Data/estabelecimentos1.csv')
    print('Terminei o Estabelecimentos 1')

    commands.loadEstabelecimentos(r'Data/estabelecimentos2.csv')
    print('Terminei o Estabelecimentos 2')

    commands.loadEstabelecimentos(r'Data/estabelecimentos3.csv')
    print('Terminei o Estabelecimentos 3')

    commands.loadEstabelecimentos(r'Data/estabelecimentos4.csv')
    print('Terminei o Estabelecimentos 4')

    commands.loadEstabelecimentos(r'Data/estabelecimentos5.csv')
    print('Terminei o Estabelecimentos 5')

    commands.loadEstabelecimentos(r'Data/estabelecimentos6.csv')
    print('Terminei o Estabelecimentos 6')

    commands.loadEstabelecimentos(r'Data/estabelecimentos7.csv')
    print('Terminei o Estabelecimentos 7')

    commands.loadEstabelecimentos(r'Data/estabelecimentos8.csv')
    print('Terminei o Estabelecimentos 8')

    commands.loadEstabelecimentos(r'Data/estabelecimentos9.csv')
    print('Terminei o Estabelecimentos 9')

    connection.disconnect()

if __name__ == '__main__':
    main()