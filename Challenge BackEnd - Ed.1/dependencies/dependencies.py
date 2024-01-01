import pyodbc
from typing import object

def connect_to_SqlServer_db() -> object:

    driver_name = r'{SQL Server}'
    server_name = r'DESKTOP-E29RO7M\SQLEXPRESS'
    database_name = r'ProjetosFrontEnd'

    conn = pyodbc.connect('Driver={};Server={};Database={}'.format(driver_name, server_name, database_name))

    return conn

