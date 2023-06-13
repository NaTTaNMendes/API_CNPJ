import time
from sqlalchemy import create_engine
from Helpers.MainHelper import MainHelper
from Model.Connection import Connection
from sqlalchemy.orm import sessionmaker
from ModelORM.Empresa import Empresa

quantidade_consulta = 100000

inicio = time.time()

connection = Connection('host', 'database', 'user', 'password')
connection.connect()
helper = MainHelper(connection)

for i in range(quantidade_consulta):
    empresa = helper.carregaEmpresa(i)

connection.disconnect()

fim = time.time()
diferenca = fim - inicio

print('tempo de execução SQL Connector: ', diferenca)


inicio = time.time()

engine = create_engine('mysql+mysqlconnector://user:password@host/database')
Session = sessionmaker(bind=engine)
session = Session()

for i in range(quantidade_consulta):
    empresa = session.query(Empresa).filter(Empresa.cnpj_base==i).first()

session.close()

fim = time.time()
diferenca = fim - inicio

print('tempo de execução ORM: ', diferenca)