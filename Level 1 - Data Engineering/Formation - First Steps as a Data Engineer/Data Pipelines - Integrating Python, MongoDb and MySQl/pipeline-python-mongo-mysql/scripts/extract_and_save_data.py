import requests 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connect_mongo(uri):
    '''
        Recebe a URI de conexão e retorna o objeto que permite a integração python + cluster MongoDb Atlas
    '''

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)    
    
    return client

def connection_to_database(client, db_name):
    '''
        Recebe o objeto de integração e o nome do database de interesse e retorna o objeto de conexão com o banco de dados correspondente
    '''

    return client[f'{db_name}']

def connection_to_collection(db_conn, collection_name):
    '''
        Recebe o objeto de conexão com o banco de dados e o nome de collection para retornar o objeto de conexão com a collection correspondente
    '''

    return db_conn[f'{collection_name}']

if __name__ == '__main__':
    print('Gerando conexão com o cluster...', end= '\n\n')
    atlas_client = connect_mongo("mongodb+srv://LucasTesteOliveira:testeTeste@cluster0.ymobupc.mongodb.net/?appName=Cluster0")

    print('Gerando conexão com daabase e sua collection...', end= '\n\n')
    db_conn = connection_to_database(atlas_client, 'Db_Teste')
    coll_conn = connection_to_collection(db_conn, 'test_collection')
    
    print('Inserindo documentos na collection...', end= '\n\n')
    coll_conn.insert_one({"Documento": "TesteConexão", "Res ponsável": "Lucas"})

    print('Pipeline executado com sucesso!')