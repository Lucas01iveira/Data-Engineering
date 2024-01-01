import pyodbc
from typing import Any

def connect_to_SqlServer_db() -> Any:

    driver_name = r'{SQL Server}'
    server_name = r'DESKTOP-E29RO7M\SQLEXPRESS'
    database_name = r'ProjetosFrontEnd'

    conn = pyodbc.connect('Driver={};Server={};Database={}'.format(driver_name, server_name, database_name))

    print('Conexão com database bem sucedida')

    return conn

# teste
if __name__ == '__main__':
    connect_to_SqlServer_db()
