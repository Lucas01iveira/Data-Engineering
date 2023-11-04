'''

* Código desenvolvido com o intuito de gerar uma API por fins didáticos 

* Sempre que uma API precisa ser desenvolvida, existem 4 pontos principais que devem ser levados em consideração:
    1) Objetivo (o que se pretende com a api)
        - Criar uma api que dsponibiliza a consulta, criação, edição e exclusão de livros   

    2) URL Base (local onde os recursos poderão ser acessados)
        - Nesse caso, localhost

    3) Endpoints (funcionalidades que serão disponibilizadas)
        - localhost/livros (get)
            - endpoint para consulta de todos os livros
        - localhost/livros (post)
            - endpoint para criar novos livros 
        - localhost/livros/id (get)
            - endpoint para consulta de livro por id
        - localhost/livros/id (put)
            - endpoint para modificação de livro com base no id
        - localhost/livros/id (delete)
            - endpoint para exclusão de livro com base no id

    4) Quais recursos serão disponibilizados
        - Livros

* Uma API nada mais é do que "um lugar" para disponibilizar recursos e/ou funcionalidades.

* De maneira geral, um endpoint nada mais é do que o endereço que a pessoa precisa chamar para obter/efetuar algum tipo de modificação dentro das funcionalidades permitidas pela API

'''

from flask import Flask, jsonify, request

app = Flask(__name__)

# Definição da lista de livros em formato dicionário (json)
# (poderia ser uma tabela dentro de um banco de dados qualquer)

livros = [
    {
        "id": 1
        ,'titulo': 'O Senhor dos Anéis - A Sociedade do Anel'
        ,'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2
        ,'titulo': 'Harry Potter e a Pedra Filosofal'
        ,'autor': 'J.K. Howling'
    },
    {
        'id': 3
        ,'titulo': 'James Clear'
        ,'autor': 'Hábitos Atômicos'
    }
]

# -- x -- -- x -- -- x -- -- x ---- x ---- x ---- x ---- x ---- x --

# Etapa de definição / construção dos endpoints

# Consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET']) 
def obtem_livro(id):
    for livro in livros:
        if (livro['id'] == id):
            return jsonify(livro)

# ao incluir o parametro <int:id> no endereço do endpoint, estamos impondo que o endereço deve receber um valor inteiro, e que esse valor inteiro será caracterizado como o parâmetro "id" passado para a função.

# Editar (id)
@app.route('/livros/<int:id>', methods=['PUT'])
def altera_livro(id):
    livro_modificado = request.get_json()
    for index_livro, livro in enumerate(livros):
        if (livro.get('id') == id):
            livros[index_livro].update(livro_modificado)

            return livros[index_livro]

# Adicionar
@app.route('/livros', methods=['POST'])
def inclui_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return novo_livro

# Excluir (id)
@app.route('/livros/<int:id>', methods=['DELETE'])
def deleta_livro(id):
    for livro in livros:
        if (livro['id'] == id):
            livros.remove(livro)
            return livro

app.run(port=5000, host='localhost', debug= True)
# -- x -- -- x -- -- x -- 