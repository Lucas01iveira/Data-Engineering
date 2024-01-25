from fastapi import Depends
from fastapi import APIRouter
from fastapi import Path
from fastapi import Response
from fastapi import HTTPException, status

from dependencies.dependencies import connect_to_sql_server_db
from models.VideoSchema import Video

import pandas as pd
from typing import Any, Dict, TypedDict
import json

router_obj = APIRouter()

@router_obj.get(
        path= '/api/v2/teste'
        ,summary= 'Testando o aplicativo.'
        ,description= 'Endpoint desenvolvido para teste de conexão / funcionamento da aplicação dentro do servidor alocado.'
        ,tags= ['Introducao']
        ,response_description='O retorno do endpoint corresponde simplesmente a um JSON informativo (não interfere no desenvolvimento/funcionamento dos demais endpoints da aplicação).'
        ,status_code=status.HTTP_200_OK
)
async def api_teste():
    return {'msg': 'isso é um teste'}

@router_obj.get(
        path= '/api/v2/videos'
        ,summary= 'Leitura da base de endereços.'
        ,description= 'Retorna uma consulta de seleção de todas as informações de endereços cadastradas/inseridas na tabela cbe.EnderecosVideos, no banco ProjetosFrontEnd.'
        ,response_description='''O retorno do endpoint corresponde a uma lista de todos os endereços de vídeos presentes na tabela correspondente do banco de dados. Essa informação é repassada ao usuário em formato JSON. 
        
        Códigos de resposta possíveis:
            - 200: Base de endereços de vídeos e informações complementares retornada com sucesso.
        '''
        ,tags=['CRUD']
        #,response_model= TypedDict[str, Video]
        #,status_code=status.HTTP_200_OK
)
async def get_videos(
    conn : Any = Depends(connect_to_sql_server_db)
):
    query = 'select * from cbe.EnderecosVideos'

    df = pd.read_sql(query, conn)
    df.set_index('id', inplace=True)

    return df.transpose().to_dict()

@router_obj.get(
        path='/api/v2/videos/{video_id}'
        ,summary='Leitura da base de endereços.'
        ,description='''Efetua uma consulta de seleção das informações de um vídeo em específico, identificado pelo Id informado. Vale destacar que o Id deve ser um número inteiro positivo.'''
        ,response_description='''O retorno do endpoint corresponde ao endereço do vídeo (e suas informações complementares) cujo id é igual ao número 'video_id'. 
        
        Códigos de resposta possíveis: 
            - 200: O Id informado está mapeado na base de dados e as informações são retornadas;
            - 404: O Id informado não está mapeado na base de dados e não há informações a serem apresentadas;
            - 422: O Id informado no endpoint não satisfaz aos requisitos de validação.
        '''
        ,tags=['CRUD']
        #,response_model= Video
)
async def get_video(
    video_id: int = Path(default=None, gt=0, description='O id do vídeo deve ser positivo')
    ,conn : Any = Depends(connect_to_sql_server_db)
):
    query = f'select * from cbe.EnderecosVideos where id = {video_id}'

    df = pd.read_sql(query, conn)
    df.set_index('id', inplace=True)

    if len(df) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Não existe nenhum vídeo com o id informado.'
        )
    else:
        return df.transpose().to_dict()
    
@router_obj.post(
        path='/api/v2/videos'
        ,summary='Criação de novo endereço na base.'
        ,description='''O método post, correspondente a esse endpoint da API, é responsável por gerar uma nova linha na tabela cbe.EnderecosVideos contendo as 3 informações principais do projeto: Titulo, Descricao e URL. Essas informações devem ser enviadas no body da requisição e, com exceção do campo de descrição, todas as demais são obrigatórias e devem satisfazer às condições de validação. Não é necessário informar o Id do endereço que estará sendo parametrizado pois a tabela no SQL Server já foi configurada para gerar um novo Id a cada insert.
        
        Condições de validação:
            - "Titulo" deve estar em formato 'title' (inicial de cada palavra em letra maiúscula);
            - "Descricao" é opcional;
            - "Url" deve ter 'projetosfrontend.com' como servidor de hospedagem do aplicativo final web (exemplo: https://www.projetosfrontend.com.br/teste).
        '''
        ,response_description='''Códigos de resposta da chamada do endpoint:
            - 201: O body da requisição foi validado corretamente e o novo cadastro foi inserido no banco;
            - 422: O body da requisição não satisfaz aos requisitos de validação.
        '''
        ,tags=['CRUD']
)
async def post_video(
    video: Video
    ,conn : Any = Depends(connect_to_sql_server_db)
): 
    
    cmd = 'insert into cbe.EnderecosVideos select '
    count = 1 
    for key, value in dict(video).items():
        if count == len(dict(video).items()):
            cmd += f'\'{value}\' as {key}'
        else:
            cmd += f'\'{value}\' as {key}, '
        count+=1

    cursor = conn.cursor()
    cursor.execute(cmd)
    cursor.commit()
    
    df_ids = pd.read_sql('select distinct id from cbe.EnderecosVideos',conn)
    df_ids.set_index('id', inplace=True)
    new_item_id = max(df_ids.index.to_list())

    query = f'select * from cbe.EnderecosVideos where id = {new_item_id}'
    df = pd.read_sql(query, conn)
    df.set_index('id', inplace=True)
    return df.transpose().to_dict()
    #return Response(status_code=status.HTTP_201_CREATED)

@router_obj.put(
        path='/api/v2/videos/{video_id}'
        ,summary='Atualização de informação na base.'
        ,description='''Atualiza, no registro com id igual a 'video_id' (passado pelo usuário), os campos "Titulo", "Descricao" e "Url" com os valores enviados pelo usuário no body da requisição. As informações no body seguem as mesmas restrições e obrigatoriedades do endpoint de post.

        Condições de validação:
            - "Titulo" deve estar em formato 'title' (inicial de cada palavra em letra maiúscula);
            - "Descricao" é opcional;
            - "Url" deve ter 'projetosfrontend.com' como servidor de hospedagem do aplicativo final web (exemplo: https://www.projetosfrontend.com.br/teste).
        '''
        ,response_description='''
        Códigos de resposta:
            - 404: O Id informado não está mapeado na base de dados e não informações a serem apresentadas;
            - 422: O Id informado no endpoint não satisfaz aos requisitos de validação.
        
        Em caso de sucesso, a API irá retornar um JSON indicando as novas informações corretamente atualizadas para o Id especificado.
        '''
        ,tags=['CRUD']
)
async def put_video(
    video: Video
    ,video_id: int = Path(default=None, gt=0, description='O id do vídeo deve ser positivo')
    ,conn : Any = Depends(connect_to_sql_server_db)
): 
    
    query = f'select * from cbe.EnderecosVideos where Id = {video_id}'
    df = pd.read_sql(query, conn)

    if len(df) == 0:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND
            ,detail= 'Não existe nenhum vídeo com o id informado'
        )
    else:
        cmd = 'update cbe.EnderecosVideos set '
        count = 1 
        for key, value in dict(video).items():
            if count == len(dict(video).items()):
                cmd += f'{key} = \'{value}\''
            else:
                cmd += f'{key} = \'{value}\', '
            count+=1

        cmd+= f' where id = {video_id}'
    
        cursor = conn.cursor()
        cursor.execute(cmd)
        cursor.commit()
        
        df = pd.read_sql(query, conn)
        df.set_index('id', inplace=True)
        return df.transpose().to_dict()

@router_obj.delete(
        path='/api/v2/videos/{video_id}'
        ,summary='Exclusão de registro na base.'
        ,description='''
        Deleta, da tabela cbe.EnderecosVideos, o registro com id igual a 'video_id'. O parâmetro em questão segue a mesma restrição dos endpoints get e put (deve ser um inteiro positivo).
        '''
        ,response_description='''Códigos de resposta:
            - 201: O registro foi excluído corretamente;
            - 404: O Id informado não está mapeado na base de dados e não informações a serem apresentadas;
            - 422: O Id informado no endpoint não satisfaz aos requisitos de validação.
        '''
        ,tags=['CRUD']
)
async def delete_video(
    video_id: int = Path(default=None, gt=0, description='O id do video deve ser um inteiro maior que 0')
    ,conn: int = Depends(connect_to_sql_server_db)
):
    query = f'select * from cbe.EnderecosVideos where id = {video_id}'

    df = pd.read_sql(query, conn)

    if len(df) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            ,detail='Não existe nenhum vídeo com o id informado'
        )
    else:
        cmd = f'delete from cbe.EnderecosVideos where id = {video_id}'

        cursor = conn.cursor()
        cursor.execute(cmd)
        cursor.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)