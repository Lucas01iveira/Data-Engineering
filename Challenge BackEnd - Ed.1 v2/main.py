from fastapi import FastAPI

from routes.routes import router_obj

app = FastAPI()
app.include_router(router=router_obj, tags=['videos'])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, debug=True, reload=True)