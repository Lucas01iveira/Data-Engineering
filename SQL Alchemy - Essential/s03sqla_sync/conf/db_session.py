import sqlalchemy as sa 

from sqlalchemy.orm import sessionmaker # para criação de sessões

from pathlib import Path # usado no sqlite
from typing import Optional # typing hint

from sqlalchemy.orm import Session 
from sqlalchemy.future.engine import Engine

from models.model_base import ModelBase # será necessário para criar/deletar tabela no banco de dados (os demais models irão ser herdados dele)

__engine: Optional[Engine] = None # criando uma variável global (ainda sem valor bruto; apenas declaração e indicação de que é do tipo Engine)

# função responsável por retornar um objeto do tipo engine
def create_engine() -> Engine:
    '''
    A engine nada mais é do que a 'configuração' da conexão do python sqlalchemy com o banco de dados à nossa escolha (nesse caso estamos tratando o sql Server)
    '''

    global __engine

    if __engine: # se a engine já estiver criada..
        return __engine
    
    # definindo a connection string para banco de dados sql server
    # 1) caso o banco tenha user/password (SQl auth)
    # conn_str = 'mssql+pyodbc://user:password@server/database'
    # sa.create_engine(conn_str)

    # 2) caso o banco possua Windows Auth (entrada direta)
    conn_str = r'mssql+pyodbc://DESKTOP-E29RO7M\SQLEXPRESS/CursoSqlAlchemy?driver=ODBC+Driver+17+for+SQL+Server'
    # é muito importante lembrar de especificar o driver, que pode ser consultado no seguinte path: Control Panel > Systems and Security > Administrative Tools > ODBC Data Sources > System DSN tab > Add
    # obs.: estamos usando a versão mais recente do driver sql (2017 // o driver mais antigo, 'SQL Server', não estava tendo a correspondência correta com o SqlAlchemy)

    __engine = sa.create_engine(url= conn_str, echo=False)

    return __engine

# função responsável por criar a sessão
def create_session() -> Session:
    '''
    Com a engine, que representa justamente a configuração de conexão e que foi criada na função anterior, podemos criar a 'sessão de conexão' ao banco de dados com o auxílio da presente função.

    É essa session que representa a conexão em si.
    '''

    global __engine # referen

    if not __engine:
        create_engine()
    
    __session = sessionmaker(__engine, expire_on_commit= False, class_= Session) # retorna um 'método'/função

    session: Session = __session()  # aplico o método retornado pela linha anterior em uma variável específica do tipo Session

    return session 

def create_tables():
    '''
    Função que utilizaremos para criar tabelas no banco de dados.
    '''

    global __engine 

    if not __engine:
        __engine = create_engine()

    import models.__all_models
    ModelBase.metadata.drop_all(__engine) # deleta todas as tabelas do banco
    ModelBase.metadata.create_all(__engine) # recria as tabelas do banco
