import mysql.connector
from mysql.connector import Error

class Connection:

    def __init__(self, host, database, user, password) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connected = False
        self.cursor = None
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )

            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print('Connecting to MySQL, version:', db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute('SELECT DATABASE()')
                record = self.cursor.fetchone()
                print('Connected to database:', record)
                self.connected = True

        except Error as e:
            print('Error connecting to MySQL: ', e)
    
    def disconnect(self):
        self.cursor.close()
        self.connection.close()
        print('Connection closed')