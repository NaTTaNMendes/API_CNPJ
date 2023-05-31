from flask import Flask
from Helpers.MainHelper import MainHelper
from Model.Connection import Connection

app = Flask(__name__)
connection = Connection('localhost', 'api_cnpj', 'root', '17102003naruto')
connection.connect()
helper = MainHelper(connection)

@app.route('/<path:text>', methods=['GET'])
def read_url_data(text): 

    response = helper.verificaCnpj(text)
    if response is not None:
        return response
    
    empresa = helper.carregaEmpresa(text)
    response = helper.retorna(empresa)
    return response

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', debug=False)