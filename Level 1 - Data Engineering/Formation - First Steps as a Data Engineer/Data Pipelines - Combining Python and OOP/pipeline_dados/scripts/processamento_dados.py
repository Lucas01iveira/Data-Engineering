import json 
import csv

class Dados:

    def __init__(self, path, tipo_dado):
        self._path = path
        self._tipo_dado = tipo_dado
        self._dados = self.read_file()
        self._nome_colunas = self.get_columns()
    
    # tornando os objetos da classe iteráveis
    def __getitem__(self, item):
        return self._dados[item]

    def __len__(self):
        return len(self._dados)

    def read_json(self):
        
        with open(self._path, 'r') as file:
            file_data = json.load(file) 
        return file_data

    def read_csv(self):
        file_data = []

        with open(self._path, 'r', encoding= 'utf-8') as file:
            reader = csv.DictReader(file, delimiter= ',')
            for row in reader:
                file_data.append(row)
        
        return file_data

    def read_file(self):
        if self._tipo_dado.upper() == 'JSON':
            return self.read_json()
        
        elif self._tipo_dado.upper() == 'CSV':
            return self.read_csv()
        
        else:
            pass

    def get_columns(self):
        return self._dados[-1].keys()
        
    def rename_columns(self, column_map: dict):
        new_file_data = []
        
        # element (type dict)
        for element in self._dados:
            new_dict = {}

            for old_column_name, value in element.items():
                new_dict[column_map[old_column_name]] = value

            new_file_data.append(new_dict)

        self._dados = new_file_data 
        self._nome_colunas = self.get_columns()

    @property
    def path(self):
        return self._path

    @property
    def tipo_dado(self):
        return self._tipo_dado
    
    @property
    def dados(self):
        return self._dados
    
    @staticmethod
    def combine_data(data1, data2, column_layout):
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

    

