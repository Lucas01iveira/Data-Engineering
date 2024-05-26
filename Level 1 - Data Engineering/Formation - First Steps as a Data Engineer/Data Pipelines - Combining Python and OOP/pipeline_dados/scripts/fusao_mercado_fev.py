import json 
import csv

def main():
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

    path_json = 'pipeline_dados/data_raw/dados_empresaA.json'
    json_data = read_file(path_json, 'json')

    # validação 
    print(json_data[0])

    path_csv = 'pipeline_dados/data_raw/dados_empresaB.csv'
    csv_data = read_file(path_csv, 'csv')

    # validação
    print(csv_data[0])

if __name__ == '__main__':
    print()
    main()
    print()