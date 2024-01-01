from fastapi import FastAPI
from fastapi import Depends

from dependencies.dependencies import connect_to_SqlServer_db

from typing import Optional, List, Any, object

import pandas as pd

app = FastAPI()

@app.get('/teste')
async def teste_api():
    return r"{'teste': 'testando', 'teste': 123}"

@app.get('/videos')
async def get_videos(
    connection: object = Depends(connect_to_SqlServer_db)
):
    df = pd.read_sql('select * from cbe.EnderecosVideos', connection)
    df.set_index('id', inplace=True)

    return df.to_json()


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, debug=True, workers=1, limit_concurrency=1, limit_max_requests=1)