from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Curso

app = FastAPI()

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


@app.get('/cursos') # definindo o endpoint (para método get)
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_cursos(curso_id: int): 
    
    # apenas por indicar o typing hint da variável em utilização o próprio fastApi já tenta fazer a conversão automaticamente (visto que tudo que entra pelo usuário é string) e, se não for possível, uma mensagem de erro é retornada.

    try:
        curso = cursos[curso_id]
        return curso
    except KeyError: # caso o usuário passe um id que não exista no nosso banco (nesse momento, hipotético)
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND
            ,details= 'Curso não encontrado')

# por padrão, o fastAPI retorna status 200 (mas para objetos criados/postados o correto seria 201), então temos que especificar manualmente dentro da definição do endpoint
@app.post('/cursos', status_code= status.HTTP_201_CREATED)  
async def post_curso(curso: Curso):
    next_id = len(cursos)+1

    del curso.id # deletando o atributo id (optional // não queremos emití-lo nas consultas)

    cursos[next_id] = curso
    return curso

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id not in cursos: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= 'O curso que você está tentando atualizar não foi encontrado no database')
    else:
        delattr(curso, 'id') # deletando o atributo id (opcional)
        cursos[curso_id].update(curso)
        return curso

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
