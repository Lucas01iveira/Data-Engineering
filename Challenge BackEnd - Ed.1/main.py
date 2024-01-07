# import de bibliotecas e módulos principais
from fastapi import FastAPI
from routers import routers_api

# início do desenvolvimento do aplicativo
app = FastAPI()

# implantação das rotas definidas no arquivo auxiliar dentro do aplicativo
app.include_router(routers_api.router, tags=['CRUD - Videos'])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, debug=True)