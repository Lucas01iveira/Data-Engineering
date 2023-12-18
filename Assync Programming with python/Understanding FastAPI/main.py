from fastapi import FastAPI # import da classe fastapi

from pydantic import BaseModel 
# por debaixo dos panos, o fastAPI utiliza esse módulo para fazer VALIDAÇÃO DE DADOS

# todos os objetos correspondentes, herdados do BaseModel, não aceitarão dados que não estejam no padrão abaixo
class Produto(BaseModel):
    id: int
    nome: str 
    preco: float 
    em_oferta: bool = False # inicializando o atributo com False

app = FastAPI() # definindo um objeto do tipo FastAPI

# definição de uma lista de objetos por fim de testes (em uma aplicação/projeto real haveria aqui uma conexão com banco de dados ou ambiente de dados semelhante)
produtos = [
    Produto(id=1, nome='Playstation 5', preco=5745.55, em_oferta=True)
    ,Produto(id=2, nome='Nintendo Wii', preco=2654.12, em_oferta=True)
    ,Produto(id=34, nome='Xbox One', preco=3686.41, em_oferta=True)
    ,Produto(id=13, nome='Super Nintendo', preco=341.34, em_oferta=True)
    ,Produto(id=4, nome='Atari 2600', preco=199.40, em_oferta=True)
]

# definição de rota get de teste
@app.get('/teste')
async def teste():
    return 'Isso é um teste!'

# definição de uma rota get
#@app.get('/')
#async def index():
#    return {'Geek':'University'}

# definição de rota get
@app.get('/produtos/{id}')
async def buscar_produto(id: int):
    for produto in produtos:
        if produto.id == id:
            return produto
        else:
            return None

# definição de rota get 
@app.get('/produtos')
async def exibir_produtos():
    return produtos

# definição de rota put
@app.put('/produtos/{id}') 
async def atualizar_produto(id: int, produto: Produto):
# a principal diferença aqui é que a variável Id deverá ser inserida na string de url e a variável produto no 'corpo' da requisição (formato json)
    for prod in produtos:
        if prod in produtos:
            prod = produto

            return prod
        else:
            return None
        