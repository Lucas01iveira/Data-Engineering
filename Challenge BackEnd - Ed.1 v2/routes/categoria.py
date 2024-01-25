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

@router_obj2.get(
        path='/api/v2/categoria'
        ,summary='Leitura da base de categorias'
        ,description='''Efetua uma leitura na tabela cbe.Categoria e retorna ao usuário um JSON contendo as informações de todas as categorias disponíveis no banco de dados.
        
        Códigos de resposta possíveis:
            - 200: requisição processada com sucesso e base retornada corretamente.
        '''
        ,tags=['CRUD - Categoria']
)
async def get_categorias(
    conn: Any = Depends(connect_to_sql_server_db)
):
    
    query = 'select * from cbe.Categoria'
    df = pd.read_sql(query, conn)
    df['CategoriaId'] = df['Id']
    df.set_index('Id', inplace=True)

    return df.transpose().to_dict()

@router_obj2.get(
        path='/api/v2/categoria/{categoria_id}'
        ,summary='Leitura da base de categorias.'
        ,description='''Efetua uma busca no banco de dados e retorna ao usuário todas as informações da categoria cujo Id é igual a 'categoria_id' (o qual deve ser um inteiro positivo).

        Códigos de resposta possíveis:
            - 200: A requisição foi processada com sucesso e houve retorno correto de dados;
            - 404: Nenhum registro com Id informado no endpoint foi encontrado;
            - 422: O parâmetro incluído no endpoint da requisição não satisfaz às regras de validação.
        '''
        ,tags=['CRUD - Categoria'])
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

@router_obj2.post(
        path='/api/v2/categoria'
        ,summary='Criação de novo registro.'
        ,description='''Essa requisição é responsável por gerar, dentro da tabela cbe.Categoria, um novo registro de categoria de acordo com as informações incluídas no body da requisição. É importante destacar que o Id desse novo registro é gerado automaticamente dentro do banco de dados no momento em que a informação é inserida, portanto não há necessidade de incluí-lo durante a chamada da requisição.

        Condições de validação:
            - "DescricaoCategoria" deve ser um campo string não vazio (ou seja, a categoria deve, obrigatoriamente, ter um "nome" ou descrição);
            - "Cor" deve ser um campo string não vazio contendo um código de cor hexadecimal que possa ser entendido pelo framework CSS.

        Códigos de resposta possíveis:
            - 200: O body da requisição foi processado corretamente e o novo registro foi inserido no banco;
            - 422: Os campos preenchidos no body da requisição não satisfazem às regras de validação.
        '''
        ,tags=['CRUD - Categoria']
        ,response_description='Além do código 200, a aplicaçao também retorna ao usuário um JSON apresentando a configuração das informações referente ao novo registro criado dentro do banco de dados.'
)
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

@router_obj2.put(
        path='/api/v2/categoria/{categoria_id}'
        ,summary='Atualização de registro.'
        ,description='''Aplica, dentro da tabela cbe.Categoria no banco de dados, a atualização do registro com Id igual a 'categoria_id' com base nas informações inseridas no body da requisição. O preenchimento do body nessa requisição segue as mesmas restrições da requisição post, assim como o parâmetro 'categoria_id' também segue a mesma restrição da requisição get correspondente.

        Condições de validação:
            - "DescricaoCategoria" deve ser um campo string não vazio (ou seja, a categoria deve, obrigatoriamente, ter um "nome" ou descrição);
            - "Cor" deve ser um campo string não vazio contendo um código de cor hexadecimal que possa ser entendido pelo framework CSS.

        Códigos de resposta possíveis:
            - 200: O body da requisição foi processado corretamente e o novo registro foi inserido no banco;
            - 404: Nenhum registro com o Id informado no endpoint foi encontrado; 
            - 422: Ou o parâmetro incluído no endpoint ou os campos preenchidos no body da requisição não satisfazem às regras de validação.
        '''
        ,tags=['CRUD - Categoria']
        ,response_description='Além do código 200, a aplicação também retorna um JSON apresentando as novas informações do registro atualizado no banco de dados.'
)
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

@router_obj2.delete(
        path='/api/v2/categoria/{categoria_id}'
        ,summary='Exclusão de registro na base.'
        ,description='''Exclui, no banco de dados, o registro da tabela cbe.Categoria cujo Id é igual ao parâmetro 'categoria_id' (que deve ser um inteiro positivo). 
        
        Códigos de resposta possíveis:
            - 201: A requisição foi processada corretamente e o registro foi deletado corretamente da base de dados;
            - 404: Nenhum registro com o Id informado no endpoint foi encontrado;
            - 422: O parâmetro inserido no endpoint não satisfaz às regras de validação.
        '''
        ,tags=['CRUD - Categoria']
)
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
