import json 
import csv

def main():
    # -- x --  -- x --  FUNÇÕES DE LEITURA DE DADOS -- x -- -- x -- 
    def read_json(path_json):

        with open(path_json, 'r') as file:
            file_data = json.load(file)
        
        return file_data

    def read_csv(path_csv):
        file_data = []

        with open(path_csv, 'r', encoding= 'utf-8') as file:
            reader = csv.DictReader(file, delimiter= ',')
            for row in reader:
                file_data.append(row)
        
        return file_data

    def read_file(file_path, file_type):
        if file_type.upper() == 'JSON':
            return read_json(file_path)
        
        elif file_type.upper() == 'CSV':
            return read_csv(file_path)
        
        else:
            pass
    
    # -- x -- -- x -- FUNÇÕES DE TRATAMENTO DE DADOS -- x -- -- x -- 

    def rename_columns(column_map: dict, file_data: list):
        new_file_data = []
        
        # element (type dict)
        for element in file_data:
            new_dict = {}

            for old_column_name, value in element.items():
                new_dict[column_map[old_column_name]] = value

            new_file_data.append(new_dict)

        return new_file_data


    def combine_data(data1: list, data2: list, column_layout: list):
        if type(data1) == list and type(data2) == list:
            total_data = []
            total_data.extend(data1)
            total_data.extend(data2)
            
            total_data_treated = []

            for item in total_data:
                new_dict = {}

                for column in column_layout:
                    new_dict[column] = item.get(column, 'INDISPONIVEL')
                
                total_data_treated.append(new_dict)

            return total_data_treated
    
        else:
            raise ValueError('Os datasets provisionados não estão no mesmo formado ou não se encontram no tipo adequado. Favor verificar.')

    #  -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x --

    
    # 1) Etapa de leitura dos dados

    path_json = 'pipeline_dados/data_raw/dados_empresaA.json'
    json_data = read_file(path_json, 'json')

    # validação
    print(json_data[0])

    path_csv = 'pipeline_dados/data_raw/dados_empresaB.csv'
    csv_data = read_file(path_csv, 'csv')

    # validação
    print(csv_data[0])

    # 2) Etapa de tratamento dos dados
    column_map = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}
    
    csv_data_renamed = rename_columns(column_map, csv_data)
    
    # validação
    print(csv_data_renamed[0])

    column_final_layout = [
        'Nome do Produto',
        'Categoria do Produto',
        'Preço do Produto (R$)',
        'Quantidade em Estoque',
        'Filial',
        'Data da Venda'
    ]
    treated_data = combine_data(json_data, csv_data_renamed, column_final_layout)

    # validacao
    print(treated_data[0])
    print(treated_data[-1])

    # 3) Etapa de disponibilização dos dados tratados 


if __name__ == '__main__':
    print()
    main()
    print()