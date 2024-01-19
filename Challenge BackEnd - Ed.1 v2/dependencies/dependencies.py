import pyodbc

def connect_to_sql_server_db():
    driver_name = '{SQL Server}'
    server_name = 'DESKTOP-E29RO7M\\SQLEXPRESS'
    database_name = 'ProjetosFrontEnd'

    connection = pyodbc.connect(f'DRIVER={driver_name};SERVER={server_name};DATABASE={database_name}')

    print('Conexão bem sucedida')

    return connection

if __name__ == '__main__':
    connect_to_sql_server_db()