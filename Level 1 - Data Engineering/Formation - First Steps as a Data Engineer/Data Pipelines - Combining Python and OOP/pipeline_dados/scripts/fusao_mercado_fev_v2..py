import json 
from processamento_dados import Dados

def read_json(path_json):

    with open(path_json, 'r') as file:
        file_data = json.load(file)
    
    return file_data


def data_pipeline():
    
    # 1) Etapa de leitura dos dados (Extract)
    print(end='\n')
    print('-- x -- '*5)

    path_json = 'pipeline_dados/data_raw/dados_empresaA.json'
    dados_empresaA = Dados(path_json, 'json')
    
    path_csv = 'pipeline_dados/data_raw/dados_empresaB.csv'
    dados_empresaB = Dados(path_csv, 'csv')

    # validação
    print('Quantidade de dados da Empresa A: {}'.format(len(dados_empresaA)))
    print('Verificando formato geral dos dados json...')
    print(dados_empresaA.dados[:1])

    print()
    print('Quantidade de dados Empresa B: {}'.format(len(dados_empresaB)))
    print('Verificando formato geral dos dados csv...')
    print(dados_empresaB.dados[:1])

    # 2) Etapa de tratamento dos dados (Transform)
    column_map = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}
    
    dados_empresaB.rename_columns(column_map)
    
    
    # validação
    print()
    print('Verificando formato geral dos dados csv após o rename das colunas...')
    print(dados_empresaB.dados[:1], end='\n\n')

    column_final_layout = [
        'Nome do Produto',
        'Categoria do Produto',
        'Preço do Produto (R$)',
        'Quantidade em Estoque',
        'Filial',
        'Data da Venda'
    ]
    
    treated_data = Dados.combine_data(dados_empresaA, dados_empresaB, column_final_layout)

    # validacao
    print('Quantidade de dados final: {}'.format(len(treated_data)))
    print('Verificando o formato geral dos dados finais a serem disponibilizados...')
    print(treated_data[0])
    print(treated_data[-1], end='\n\n')

    # # 3) Etapa de disponibilização dos dados tratados 
    # path_to_save = r'pipeline_dados/data_processed/dados_combinados_fev.csv'

    # print('Iniciando processo de disponibilização do arquivo unificado...')
    # save_file(path_to_save, treated_data, column_final_layout)
    # print('Arquivo final processado com sucesso!')

    print('-- x -- '*5)
    print(end='\n')

if __name__ == '__main__':
    data_pipeline()