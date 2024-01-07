from fastapi import APIRouter # import do módulo de construção dos routers
from fastapi import Depends
from fastapi import Path
from fastapi import Response
from fastapi import HTTPException, status

from dependencies.dependencies import connect_to_SqlServer_db
from models.VideoSchema import Video

from typing import Any, List
import pandas as pd 


router = APIRouter() # definição do objeto construtor das rotas

@router.get('teste')
async def teste_api():
    return r"{'teste': 'testando', 'teste': 123}"

@router.get('videos')
async def get_videos(
    connection: Any = Depends(connect_to_SqlServer_db)
):
    df = pd.read_sql('select * from cbe.EnderecosVideos', connection)
    df.set_index('id', inplace=True)

    # da maneira que a função to_dict funciona, estávamos retornando, para cada coluna, todas linhas referentes aos videos;e gostaríamos de retornar, na verdade, todas as colunas para cada linha;

    # por esse motivo, aplicamos um transpose no dataframe antes de aplicar o to_dict; dessa forma as colunas tornam-se os id's de cada vídeo e, assim, temos de fato para cada coluna (ou seja, para cada video) todos os seus dados subsequentes

    return df.transpose().to_dict()

@router.get('videos/{video_id}')
async def get_video(
    video_id: int = Path(default=None, gt=0, description='O id do vídeo deve ser um número maior que 0'),
    connection: Any = Depends(connect_to_SqlServer_db)
):  
    
    query = f'''
            select * from cbe.EnderecosVideos where Id = {video_id}
        '''
    
    df = pd.read_sql(query, connection)
    df.set_index('id', inplace=True)
    #df = df.transpose()

    if len(df) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            ,detail='Vídeo não encontrado no database de trabalho'
        )
    else:
        return df.transpose().to_dict()
    
@router.delete('videos/{video_id}')
async def delete_video(
    video_id: int = Path(default=None, gt=0,description= 'O id do vídeo deve ser um número maior que 0'),
    connection: Any = Depends(connect_to_SqlServer_db)
):
    query = f'''
        select * from cbe.EnderecosVideos where Id = {video_id}
    '''

    df = pd.read_sql(query, connection)
    if len(df) == 0:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND
            ,detail='Vídeo não encontrado no database de trabalho'
        )

    else:
        cursor = connection.cursor()
        cmd = 'delete from cbe.EnderecosVideos where id = {}'.format(video_id)
        cursor.execute(cmd)
        cursor.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
@router.put('videos/{video_id}')
async def update_video(
    video: Video,
    video_id: int = Path(default=None, gt=0, description='O id do vídeo deve ser um número maior que 0'),
    connection: Any = Depends(connect_to_SqlServer_db)
):
  query = 'select * from cbe.EnderecosVideos where id = {}'.format(video_id)
  df = pd.read_sql(query, connection)

  if len(df) == 0:
      raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND
          ,detail='Vídeo não encontrado no database de trabalho'
      )
  else:
    cmd = 'update cbe.EnderecosVideos set '
    counter = 1
    for column,value in dict(video).items():
        if counter == len(dict(video)):
            cmd += f'{column} = \'{value}\' '
        else:
            cmd += f'{column} = \'{value}\', '
        counter += 1

        
    cmd += f'where id = {video_id}'

    cursor = connection.cursor()
    cursor.execute(cmd)
    cursor.commit()
    return Response(status_code=status.HTTP_202_ACCEPTED)
  
@router.post('videos')
async def update_video(
    video: Video,
    connection: Any = Depends(connect_to_SqlServer_db)
):
  
    cmd = f'insert into cbe.EnderecosVideos select '
    counter = 1
    for column,value in dict(video).items():
        if counter == len(dict(video)):
            cmd += f'\'{value}\' as {column} '
        else:
            cmd += f'\'{value}\' as {column}, '
        counter += 1

    
    cursor = connection.cursor()
    cursor.execute(cmd)
    cursor.commit()
    return Response(status_code=status.HTTP_201_CREATED)