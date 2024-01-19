from fastapi import Depends
from fastapi import APIRouter
from fastapi import Path
from fastapi import Response
from fastapi import HTTPException, status

from dependencies.dependencies import connect_to_sql_server_db
from models.VideoSchema import Video

import pandas as pd
from typing import Any
import json

router_obj = APIRouter()

@router_obj.get('/api/v2/teste')
async def api_teste():
    return {'msg': 'isso é um teste'}

@router_obj.get('/api/v2/videos')
async def get_videos(
    conn : Any = Depends(connect_to_sql_server_db)
):
    query = 'select * from cbe.EnderecosVideos'

    df = pd.read_sql(query, conn)
    df.set_index('id', inplace=True)

    return df.transpose().to_dict()

@router_obj.get('/api/v2/videos/{video_id}')
async def get_videos(
    video_id: int = Path(default=None, gt=0, description='O id do vídeo deve ser positivo')
    ,conn : Any = Depends(connect_to_sql_server_db)
):
    query = f'select * from cbe.EnderecosVideos where id = {video_id}'

    df = pd.read_sql(query, conn)
    df.set_index('id', inplace=True)

    if len(df) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Não existe nenhum vídeo com o id informado'
        )
    else:
        return df.transpose().to_dict()
    
@router_obj.post('/api/v2/videos')
async def get_videos(
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
    
    return Response(status_code=status.HTTP_201_CREATED)

@router_obj.put('/api/v2/videos/{video_id}')
async def get_videos(
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

@router_obj.delete('/api/v2/videos/{video_id}')
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