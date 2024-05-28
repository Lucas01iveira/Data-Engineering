import json 
import csv

class Dados:

    def __init__(self, path: str, tipo_dado: str) -> object:
        self._path = path
        self._tipo_dado = tipo_dado
        self._dados = self.read_file()
        self._nome_colunas = self.get_columns()
    
    # tornando os objetos da classe iteráveis
    def __getitem__(self, item) -> None:
        return self._dados[item]

    def __len__(self) -> int:
        return len(self._dados)

    def read_json(self) -> list:
        
        with open(self._path, 'r') as file:
            file_data = json.load(file) 
        return file_data

    def read_csv(self) -> list:
        file_data = []

        with open(self._path, 'r', encoding= 'utf-8') as file:
            reader = csv.DictReader(file, delimiter= ',')
            for row in reader:
                file_data.append(row)
        
        return file_data

    def read_file(self) -> list:
        if self._tipo_dado.upper() == 'JSON':
            return self.read_json()
        
        elif self._tipo_dado.upper() == 'CSV':
            return self.read_csv()
        
        elif self._tipo_dado.upper() == 'LIST':
            dados = self._path
            self._path = 'lista de registros definida em memória'
            return dados

        else:
            pass

    def get_columns(self) -> list:
        return self._dados[-1].keys()
        
    def rename_columns(self, column_map: dict) -> object:
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
    def path(self) -> str:
        return self._path

    @property
    def tipo_dado(self) -> str:
        return self._tipo_dado
    
    @property
    def dados(self) -> str:
        return self._dados
    
    @staticmethod
    def combine_data(data1 : object, data2: object, column_layout: dict) -> object:
        total_data = []
        total_data.extend(data1)
        total_data.extend(data2)
        
        total_data_treated = []

        for item in total_data:
            new_dict = {}

            for column in column_layout:
                new_dict[column] = item.get(column, 'INDISPONIVEL')
            
            total_data_treated.append(new_dict)

        return Dados(total_data_treated, 'list')

    @staticmethod
    def save_file(path: str, related_data: object, column_layout: list) -> None:
        with open(path, 'w', encoding= 'utf-8') as file:
            file_writer = csv.DictWriter(file, fieldnames= column_layout)
            file_writer.writeheader()
            file_writer.writerows(related_data)

