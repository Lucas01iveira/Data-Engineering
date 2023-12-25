from typing import List, Optional, Any # classes de typing hints
from fastapi import FastAPI # classe de definição do aplicativo
from fastapi import HTTPException # classe para retorno do objeto HttpException
from fastapi import status # constante com códigos de de resposta http (para cada tipo de log) 
from fastapi import Response # classe para retorno da resposta 204 (no content / endpoint delete)
from fastapi import Path # classe auxiliar de validação do parâmetro passado no endpoint get (path)
from fastapi import Query # classe auxiliar de validação do parâmetro passado na query do endpoint get
from fastapi import Header # classe auxiliar de validação do header da requisição get
from fastapi import Depends # classe auxiliar para definição de dependências
from fastapi.responses import JSONResponse # classe para retorno da resposta 204 (ainda em dev)
from models import Curso # classe curso (referente ao projeto da nossa aplicação)

from time import sleep

# acesso da documentação no navegador:
# http://localhost:<numero_da_porta>/docs
# http://localhost:<numero_da_porta>/redoc

# podemos alterar os parâmetros da classe FastAPI para enriquecermos a documentação (consultar a classe para identificação dos parâmetros possíveis)
app = FastAPI(
    title= 'API didática - curso Udemy'
    ,version= '0.0.1'
    ,description='API criada com a finalidade de estudar as funções'
)

cursos = {
    1: {
        'titulo': 'Programação para Leigos'
        ,'aulas': 112
        ,'horas': 58
    },
    2: {
        'titulo': 'Algoritmos e Lógica de Programação'
        ,'aulas': 87
        ,'horas': 75
    }
}

def conecta_database():
    print('Conectando database', end='')
    for _ in range(3):
        if _ == 2:
            print('.')
            sleep(1)
        else:
            print('.', end='')
            sleep(1)
    print('Desligando database', end='')
    for _ in range(3):
        if _ == 2:
            print('.')
            sleep(1)
        else:
            print('.', end='')
            sleep(1)
    

# método de consulta (GET)
@app.get('/cursos') # definindo o endpoint (para método get)
async def get_cursos(db: Any = Depends(conecta_database)):
    return cursos

# método de consulta (GET)
@app.get('/cursos/{curso_id}')
async def get_cursos(
    curso_id: int = Path(default=None, description= 'O Id deve estar entre 0 e 3', gt=0, lt=3)
    ,db: Any = Depends(conecta_database)
    ): 
    
    # apenas por indicar o typing hint da variável em utilização o próprio fastApi já tenta fazer a conversão automaticamente (visto que tudo que entra pelo usuário é string) e, se não for possível, uma mensagem de erro é retornada.

    try:
        curso = cursos[curso_id]
        return curso
    except KeyError: # caso o usuário passe um id que não exista no nosso banco (nesse momento, hipotético)
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND
            ,details= 'Curso não encontrado')

# método de criação/geração de dados (POST)
# por padrão, o fastAPI retorna status 200 (mas para objetos criados/postados o correto seria 201), então temos que especificar manualmente dentro da definição do endpoint
@app.post('/cursos', status_code= status.HTTP_201_CREATED)  
async def post_curso(
    curso: Curso
    ,db: Any = Depends(conecta_database)
    ):
    next_id = len(cursos)+1

    del curso.id # deletando o atributo id (optional // não queremos emití-lo nas consultas)

    cursos[next_id] = curso
    return curso

# método de atualização (PUT)
@app.put('/cursos/{curso_id}')
async def put_curso(
    curso_id: int
    , curso: Curso, db: Any = Depends(conecta_database)
    ):
    if curso_id not in cursos: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= 'O curso que você está tentando atualizar não foi encontrado no database')
    else:
        delattr(curso, 'id') # deletando o atributo id (opcional)
        cursos[curso_id].update(curso)
        return curso

# método para exclusão de dados (DELETE)
@app.delete('/cursos/{curso_id}')
async def delete_curso(
    curso_id: int
    ,db: Any = Depends(conecta_database)
    ):
    if curso_id not in cursos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            ,detail= 'O curso que você está tentando atualizar não foi encontrado no database'
        )
    else:
        del cursos[curso_id]
        #return JSONResponse(status_code=status.HTTP_204_NO_CONTENT) # por enquanto o json response não está 100% implementado (Sem bugs)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

# -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x ---- x --

# método extra apenas para entendimento das query parameters
@app.get('/calculadora')
async def calculadora(
        a: int = Query(default=None, gt=0, lt=5) # validando query parameter
        , x_geek: str = Header(default=None) # validando header parameter
        , b: int = Query(default=None, gt=3, lt=10) # validando query parameter
        , c: Optional[int] = 0 # query parameter opcional
    ):
    soma = a+b+c
    print('X-GEEK: {}'.format(x_geek)) 
    # '_' deve ser passado como '-' no header quando a requisição estiver sendo feita

    return {'resultado': soma}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, debug=True, reload= True)
    # parâmetros fornecidos:
        # file_name no qual o app se encontra
        # host: servidor no qual o app se encontra// nesse caso estamos fazendo localmente)
            # a inclusão do 0.0.0.0 permite que qualquer outro usuário desenvolva o projeto sem ser barrado pelo IP do computador
        # port: porta da rede (determina o local, dentro do sistema operacional do computador, em que as conexões começam e terminam)
    # debug: flag indicativa de execuções de teste ou não
    # reload: flag indicativa de reinicialização da aplicação sempre que uma nova alteração é aplicada
