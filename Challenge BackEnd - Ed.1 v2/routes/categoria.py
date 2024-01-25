from fastapi import APIRouter 
from fastapi import Depends
from fastapi import Path
from fastapi import Response
from fastapi import HTTPException, status

from dependencies.dependencies import connect_to_sql_server_db
from models.CategoriaSchema import Categoria
from typing import Any

import pandas as pd

router_obj2 = APIRouter()

@router_obj2.get(
        path='/api/v2/categoria/teste'
        ,summary='Testando o aplicativo'
        ,description='Endpoint desenvolvido para teste de conexão / funcionamento da aplicação dentro do servidor alocado.'
        ,tags=['Introducao'])
async def get_teste():
    return {'msg': 'isso é um teste'}

@router_obj2.get('/api/v2/categoria')
async def get_categorias(
    conn: Any = Depends(connect_to_sql_server_db)
):
    
    query = 'select * from cbe.Categoria'
    df = pd.read_sql(query, conn)
    df['CategoriaId'] = df['Id']
    df.set_index('Id', inplace=True)

    return df.transpose().to_dict()

@router_obj2.get('/api/v2/categoria/{categoria_id}')
async def get_categoria(
    categoria_id: int = Path(default=None, gt=0, description='O Id da categoria deve ser um inteiro positivo.')
    ,conn: Any = Depends(connect_to_sql_server_db)
):
    
    query = f'select * from cbe.Categoria where Id = {categoria_id}'
    df = pd.read_sql(query, conn)
    
    if len(df) == 0:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            ,detail='Não existe nenhuma categoria com o Id informado.'
        )
    else:
        df['CategoriaId'] = df['Id']
        df.set_index('Id', inplace=True)
        return df.transpose().to_dict()

@router_obj2.post('/api/v2/categoria')
async def post_categoria(
    categoria: Categoria
    ,conn: Any = Depends(connect_to_sql_server_db)
):
    
    cmd = 'insert into cbe.Categoria select '
    counter = 1
    for key, value in dict(categoria).items():
        if counter == len(dict(categoria).items()):
            cmd += f'\'{value}\' as {key}'
        else:
            cmd += f'\'{value}\' as {key}, '
        counter += 1
    
    cursor = conn.cursor()
    cursor.execute(cmd)
    cursor.commit()

    select_novo_registro = 'select * from cbe.Categoria where Id = (select max(Id) from cbe.Categoria)'
    df = pd.read_sql(select_novo_registro, conn)
    df['CategoriaId'] = df['Id']
    df.set_index('Id', inplace=True)

    return df.transpose().to_dict()

@router_obj2.put('/api/v2/categoria/{categoria_id}')
async def post_categoria(
    categoria: Categoria
    ,categoria_id: int = Path(default=None, gt=0, description='O Id da categoria deve ser um inteiro positivo.')
    ,conn: Any = Depends(connect_to_sql_server_db)
):
    
    query_aux = f'select * from cbe.Categoria where Id = {categoria_id}'
    df_aux = pd.read_sql(query_aux, conn)

    if len(df_aux) == 0:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            ,detail='Não existe nenhuma categoria com o Id informado.'
        )
    else:
        cmd = 'update cbe.Categoria set '
        counter = 1
        for key, value in dict(categoria).items():
            if counter == len(dict(categoria).items()):
                cmd += f'{key} = \'{value}\' '
            else:
                cmd += f'{key} = \'{value}\', '
            counter += 1
        
        cmd += f'where Id = {categoria_id}'

        #return cmd
        cursor = conn.cursor()
        cursor.execute(cmd)
        cursor.commit()

        query = f'select * from cbe.Categoria where Id = {categoria_id}'
        df = pd.read_sql(query, conn)
        df['CategoriaId'] = df['Id']
        df.set_index('Id', inplace=True)

        return df.transpose().to_dict()

@router_obj2.delete('/api/v2/categoria/{categoria_id}')
async def delete_categoria(
    categoria_id: int = Path(default=None, gt=0, description='O Id da categoria deve ser um inteiro positivo.')
    ,conn: Any = Depends(connect_to_sql_server_db)
):
    
    query_aux = f'select * from cbe.Categoria where Id = {categoria_id}'
    df_aux = pd.read_sql(query_aux, conn)

    if len(df_aux) == 0:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            ,detail='Não existe nenhuma categoria com o Id informado.'
        )
    else:
        cmd = f'delete from cbe.Categoria where Id = {categoria_id}' 

        cursor = conn.cursor()
        cursor.execute(cmd)
        cursor.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)
