from fastapi import FastAPI
from routers import curso
from routers import usuario

app = FastAPI()

app.include_router(curso.router, tags=['cursos'])
app.include_router(usuario.router, tags=['usuarios'])

if __name__ == '__main__':
    import uvicorn 

    uvicorn.run('main:app', host='0.0.0.0', port=8000, debug=True, reload= True)
