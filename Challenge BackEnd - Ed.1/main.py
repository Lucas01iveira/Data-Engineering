# import de bibliotecas e módulos principais
from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException, status

from dependencies.dependencies import connect_to_SqlServer_db

from typing import Any, Optional, List

import pandas as pd

# -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- 

# início do desenvolvimento do aplicativo
app = FastAPI()

@app.get('/teste')
async def teste_api():
    return r"{'teste': 'testando', 'teste': 123}"

@app.get('/videos')
async def get_videos(
    connection: Any = Depends(connect_to_SqlServer_db)
):
    df = pd.read_sql('select * from cbe.EnderecosVideos', connection)
    df.set_index('id', inplace=True)

    # da maneira que a função to_dict funciona, estávamos retornando, para cada coluna, todas linhas referentes aos videos;e gostaríamos de retornar, na verdade, todas as colunas para cada linha;

    # por esse motivo, aplicamos um transpose no dataframe antes de aplicar o to_dict; dessa forma as colunas tornam-se os id's de cada vídeo e, assim, temos de fato para cada coluna (ou seja, para cada video) todos os seus dados subsequentes

    return df.transpose().to_dict()

@app.get('/videos/{curso_id}')
async def get_video(
    curso_id: int,
    connection: Any = Depends(connect_to_SqlServer_db)
):  
    
    query = f'''
            select * from cbe.EnderecosVideos where Id = {curso_id}
        '''
    
    df = pd.read_sql(query, connection)
    df.set_index('id', inplace=True)
    #df = df.transpose()

    if len(df) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            ,detail='Video não encontrado no database de trabalho'
        )
    else:
        return df.transpose().to_dict()


if __name__ == '__main__':
    import uvicorn

    #uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, debug=True, workers=1, limit_concurrency=1, limit_max_requests=1)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, debug=True)