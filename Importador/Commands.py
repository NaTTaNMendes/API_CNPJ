import pandas as pd
import math
import numpy as np

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
    
    def loadMotivo(self, filename):
        try:

            file = pd.read_csv(filename, delimiter=';', encoding='latin-1')

            for _, row in file.iterrows():

                reason_value = row[0]
                description_value = row[1]

                insert_query = '''
                    INSERT INTO {table} (codigo_motivo, descricao)
                    VALUES ('{code}', '{description}') ON DUPLICATE KEY UPDATE 
                    codigo_motivo={code}, descricao="{description}"
                '''.format(
                    table='motivo',
                    code=reason_value,  
                    description=description_value
                )
                self.connection.cursor.execute(insert_query)
                self.connection.connection.commit()
            
            print('motivo table updated')

        except Exception as e:
            print('Error populating Motivo: ', e)
    
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
    
    def loadMunicipio(self, filename):
        try:
            
            file = pd.read_csv(filename, delimiter=';', encoding='latin-1')

            for _, row in file.iterrows():            
                city_value = row[0]
                name_value = row[1].replace("'", "")

                insert_query = '''
                    INSERT INTO {table} (codigo_municipio, nome)
                    VALUES ('{code}', '{name}') ON DUPLICATE KEY UPDATE 
                    codigo_municipio={code}, nome="{name}"
                '''.format(
                    table='municipio',
                    code=city_value,  
                    name=name_value
                )
                self.connection.cursor.execute(insert_query)
                self.connection.connection.commit()
            
            print('municipio table updated')

        except Exception as e:
            print('Error populating municipio: ', e)
    
    def loadSocio(self, filename, id_value):
        try:
            file = pd.read_csv(filename, delimiter=';', encoding='latin-1')

            # Fetch country codes from the 'pais' table
            query = "SELECT codigo_pais FROM pais"
            self.connection.cursor.execute(query)
            country_codes = [row[0] for row in self.connection.cursor.fetchall()]

            # Same for qualificacao_socio
            query = "SELECT codigo_qualificacao FROM qualificacao_socio"
            self.connection.cursor.execute(query)
            qualification_codes = [row[0] for row in self.connection.cursor.fetchall()]

            id_value += 1

            for line_number, row in file.iterrows():
                itens = list(row)[:11]
                itens.insert(0, id_value)

                # Replace '*' with None for cnpj_cpf_socio and representante_cpf
                itens[4] = itens[4].replace('*', '') if isinstance(itens[4], str) else itens[4]
                itens[8] = itens[8].replace('*', '') if isinstance(itens[8], str) else itens[8]

                # Set default value for codigo_pais if it's not in country_codes
                if itens[7] not in country_codes:
                    itens[7] = 999
                
                if itens[5] not in qualification_codes:
                    itens[5] = 999

                # Replace NaN values with None
                itens = [None if isinstance(item, float) and math.isnan(item) else item for item in itens]

                insert_query = '''
                    INSERT INTO socio (id, cnpj_base, identificador, nome,
                    cnpj_cpf_socio, codigo_qualificacao, entrada_sociedade,
                    codigo_pais, representante_cpf, nome_representante,
                    qualificacao_representante, faixa_etaria)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                    id = VALUES(id), 
                    cnpj_base = VALUES(cnpj_base),
                    identificador = VALUES(identificador),
                    nome = VALUES(nome),
                    cnpj_cpf_socio = VALUES(cnpj_cpf_socio),
                    codigo_qualificacao = VALUES(codigo_qualificacao),
                    entrada_sociedade = VALUES(entrada_sociedade),
                    codigo_pais = VALUES(codigo_pais),
                    representante_cpf = VALUES(representante_cpf),
                    nome_representante = VALUES(nome_representante),
                    qualificacao_representante = VALUES(qualificacao_representante),
                    faixa_etaria = VALUES(faixa_etaria)
                '''

                self.connection.cursor.execute(insert_query, itens)
                self.connection.connection.commit()
                id_value += 1
                print('Inserted line ' + str(line_number + 2))

            print('socio table updated')

        except Exception as e:
            print(itens)
            print('Error populating socio:', e)
    
    def loadSimples(self, filename):
        try:
            file = pd.read_csv(filename, delimiter=';', encoding='latin-1', header=None)

            insert_query = '''
                INSERT INTO simples (cnpj_base, opcao_simples, data_opcao_simples,
                data_exclusao_simples, opcao_mei, data_opcao_mei, data_exclusao_mei)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                opcao_simples = VALUES(opcao_simples),
                data_opcao_simples = VALUES(data_opcao_simples),
                data_exclusao_simples = VALUES(data_exclusao_simples),
                opcao_mei = VALUES(opcao_mei),
                data_opcao_mei = VALUES(data_opcao_mei),
                data_exclusao_mei = VALUES(data_exclusao_mei)
            '''

            rows_to_insert = []
            for line_number, row in file.iterrows():
                row_values = row[:7].tolist()

                row_values[2] = 18891201 if row_values[2] == 0 else row_values[2]
                row_values[3] = 18891201 if row_values[3] == 0 else row_values[3]
                row_values[5] = 18891201 if row_values[5] == 0 else row_values[5]
                row_values[6] = 18891201 if row_values[6] == 0 else row_values[6]

                rows_to_insert.append(row_values)

                if len(rows_to_insert) == 50000:
                    self.connection.cursor.executemany(insert_query, rows_to_insert)
                    self.connection.connection.commit()
                    rows_to_insert = []  

            if len(rows_to_insert) > 0:
                self.connection.cursor.executemany(insert_query, rows_to_insert)
                self.connection.connection.commit()

            print('simples table updated')

        except Exception as e:
            print('Error populating simples:', e)


    def loadEmpresas(self, filename):
        try:
            file = pd.read_csv(filename, delimiter=';', encoding='latin-1', header=None)

            query = "SELECT codigo_qualificacao FROM qualificacao_socio"
            self.connection.cursor.execute(query)
            qualification_codes = [row[0] for row in self.connection.cursor.fetchall()]

            query = "SELECT codigo_natureza FROM natureza"
            self.connection.cursor.execute(query)
            nature_codes = [row[0] for row in self.connection.cursor.fetchall()]

            insert_query = '''
                INSERT INTO empresa (cnpj_base, razao_social, codigo_natureza,
                qualificacao_responsavel, capital_social, porte_empresa, ente_federativo)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                razao_social = VALUES(razao_social),
                codigo_natureza = VALUES(codigo_natureza),
                qualificacao_responsavel = VALUES(qualificacao_responsavel),
                capital_social = VALUES(capital_social),
                porte_empresa = VALUES(porte_empresa),
                ente_federativo = VALUES(ente_federativo)
            '''

            rows_to_insert = []
            for line_number, row in file.iterrows():
                row_values = row[:7].tolist()

                if not row_values[2] in nature_codes:
                    row_values[2] = 9999
                
                if not row_values[3] in qualification_codes:
                    row_values[3] = 999

                row_values[4] = row_values[4].replace(',', '.')

                row_values = [None if isinstance(value, float) and math.isnan(value) else value for value in row_values]

                rows_to_insert.append(row_values)

                if len(rows_to_insert) == 500000:
                    self.connection.cursor.executemany(insert_query, rows_to_insert)
                    self.connection.connection.commit()
                    rows_to_insert = [] 

            if len(rows_to_insert) > 0:
                self.connection.cursor.executemany(insert_query, rows_to_insert)
                self.connection.connection.commit()

            print('empresa table updated')

        except Exception as e:
            print('Error populating empresa:', e)

    def loadEstabelecimentos(self, filename):
        try:
            chunk_size = 100000

            query = "SELECT codigo_motivo FROM motivo"
            self.connection.cursor.execute(query)
            reason_codes = [row[0] for row in self.connection.cursor.fetchall()]

            query = "SELECT codigo_pais FROM pais"
            self.connection.cursor.execute(query)
            country_codes = [row[0] for row in self.connection.cursor.fetchall()]

            query = "SELECT codigo_cnae FROM cnae"
            self.connection.cursor.execute(query)
            cnae_codes = [row[0] for row in self.connection.cursor.fetchall()]

            query = "SELECT codigo_municipio FROM municipio"
            self.connection.cursor.execute(query)
            city_codes = [row[0] for row in self.connection.cursor.fetchall()]

            insert_query = '''
                INSERT INTO estabelecimento (cnpj_base, cnpj_ordem, cnpj_dv, identificador_matriz,
                nome_fantasia, situacao_cadastral, data_situacao_cadastral, codigo_motivo,
                nome_cidade_exterior, codigo_pais, inicio_atividade, codigo_cnae_principal,
                tipo_logradouro, logradouro, numero, complemento, bairro, cep, uf, codigo_municipio,
                ddd1, telefone1, ddd2, telefone2, ddd_fax, fax, email, situacao_especial,
                data_situacao_especial)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                cnpj_ordem = VALUES(cnpj_ordem),
                cnpj_dv = VALUES(cnpj_dv),
                identificador_matriz = VALUES(identificador_matriz),
                nome_fantasia = VALUES(nome_fantasia),
                situacao_cadastral = VALUES(situacao_cadastral),
                data_situacao_cadastral = VALUES(data_situacao_cadastral),
                codigo_motivo = VALUES(codigo_motivo),
                nome_cidade_exterior = VALUES(nome_cidade_exterior),
                codigo_pais = VALUES(codigo_pais),
                inicio_atividade = VALUES(inicio_atividade),
                codigo_cnae_principal = VALUES(codigo_cnae_principal),
                tipo_logradouro = VALUES(tipo_logradouro),
                logradouro = VALUES(logradouro),
                numero = VALUES(numero),
                complemento = VALUES(complemento),
                bairro = VALUES(bairro),
                cep = VALUES(cep),
                uf = VALUES(uf),
                codigo_municipio = VALUES(codigo_municipio),
                ddd1 = VALUES(ddd1),
                telefone1 = VALUES(telefone1),
                ddd2 = VALUES(ddd2),
                telefone2 = VALUES(telefone2),
                ddd_fax = VALUES(ddd_fax),
                fax = VALUES(fax),
                email = VALUES(email),
                situacao_especial = VALUES(situacao_especial),
                data_situacao_especial = VALUES(data_situacao_especial)
            '''

            for chunk in pd.read_csv(filename, delimiter=';', encoding='latin-1', header=None, chunksize=chunk_size):

                rows_to_insert = []
                for line_number, row in chunk.iterrows():
                    row_values = row[:30].tolist()
                    row_values.pop(12) #remove the column that have multiple itens
                    row_values[0] = int(row_values[0])  # Convert cnpj_base to bigint

                    if not row_values[7] in reason_codes:
                        row_values[7] = 999
                    
                    if not row_values[9] in country_codes:
                        row_values[9] = 999
                    
                    if not row_values[11] in cnae_codes:
                        row_values[11] = 0
                    
                    if not row_values[19] in city_codes:
                        row_values[19] = 100000
                    
                    try:
                        row_values[17] = int(row_values[17])
                    except:
                        pass

                    try:
                        row_values[20] = int(row_values[20])
                    except:
                        pass

                    try:
                        row_values[21] = int(row_values[21])
                    except:
                        pass

                    try:
                        row_values[22] = int(row_values[22])
                    except:
                        pass

                    try:
                        row_values[23] = int(row_values[23])
                    except:
                        pass

                    try:
                        row_values[24] = int(row_values[24])
                    except:
                        pass

                    try:
                        row_values[25] = int(row_values[25])
                    except:
                        pass
                    
                    row_values = [None if isinstance(value, float) and math.isnan(value) else value for value in row_values]
                    
                    row_values[6] = 18891201 if row_values[6] == 0 else row_values[6]
                    row_values[10] = 18891201 if row_values[10] == 0 else row_values[10]
                    row_values[28] = 18891201 if row_values[28] == None else row_values[28]              

                    rows_to_insert.append(row_values)

                    if len(rows_to_insert) == 100000:
                        self.connection.cursor.executemany(insert_query, rows_to_insert)
                        self.connection.connection.commit()
                        rows_to_insert = []

                if len(rows_to_insert) > 0:
                    self.connection.cursor.executemany(insert_query, rows_to_insert)
                    self.connection.connection.commit()

            print('estabelecimento table updated')

        except Exception as e:
            print('Error populating estabelecimento:', e)