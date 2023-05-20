import pandas as pd

class Commands:

    def __init__(self, connection) -> None:
        self.connection = connection
    
    def loadCnae(self, filename):
        try:

            file = pd.read_csv(filename, delimiter=';', encoding='latin-1')

            for _, row in file.iterrows():

                cnae_value = row[0]
                description_value = row[1]

                insert_query = '''
                    INSERT INTO {table} (codigo_cnae, descricao)
                    VALUES ('{code}', '{description}') ON DUPLICATE KEY UPDATE 
                    codigo_cnae={code}, descricao="{description}"
                '''.format(
                    table='cnae',
                    code=cnae_value,  
                    description=description_value
                )
                self.connection.cursor.execute(insert_query)
                self.connection.connection.commit()
            
            print('cnae table updated')

        except Exception as e:
            print('Error populating Cnae: ', e)
    
    def loadNaturezaJuridica(self, filename):
        try:
            
            file = pd.read_csv(filename, delimiter=';', encoding='latin-1')

            for _, row in file.iterrows():            
                nature_value = row[0]
                description_value = row[1]

                insert_query = '''
                    INSERT INTO {table} (codigo_natureza, descricao)
                    VALUES ('{code}', '{description}') ON DUPLICATE KEY UPDATE 
                    codigo_natureza={code}, descricao="{description}"
                '''.format(
                    table='natureza',
                    code=nature_value,  
                    description=description_value
                )
                self.connection.cursor.execute(insert_query)
                self.connection.connection.commit()
            
            print('natureza table updated')

        except Exception as e:
            print('Error populating natureza: ', e)
    
    def loadPais(self, filename):
        try:
            
            file = pd.read_csv(filename, delimiter=';', encoding='latin-1')

            for _, row in file.iterrows():            
                country_value = row[0]
                name_value = row[1]

                insert_query = '''
                    INSERT INTO {table} (codigo_pais, nome)
                    VALUES ('{code}', '{name}') ON DUPLICATE KEY UPDATE 
                    codigo_pais={code}, nome="{name}"
                '''.format(
                    table='pais',
                    code=country_value,  
                    name=name_value
                )
                self.connection.cursor.execute(insert_query)
                self.connection.connection.commit()
            
            print('pais table updated')

        except Exception as e:
            print('Error populating pais: ', e)
    
    def loadQualificacaoSocio(self, filename):
        try:
            
            file = pd.read_csv(filename, delimiter=';', encoding='latin-1')

            for _, row in file.iterrows():            
                qualification_value = row[0]
                description_value = row[1]

                insert_query = '''
                    INSERT INTO {table} (codigo_qualificacao, descricao)
                    VALUES ('{code}', '{description}') ON DUPLICATE KEY UPDATE 
                    codigo_qualificacao={code}, descricao="{description}"
                '''.format(
                    table='qualificacao_socio',
                    code=qualification_value,  
                    description=description_value
                )
                self.connection.cursor.execute(insert_query)
                self.connection.connection.commit()
            
            print('qualificacao_socio table updated')

        except Exception as e:
            print('Error populating qualificacao_socio: ', e)