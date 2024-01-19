from fastapi import FastAPI

from routes.routes import router_obj

app = FastAPI(
    title='Armazenamento de Url\'s'
    ,description='API designada a controlar a movimentação de atualizações na tabela cbe.EnderecosVideos do banco de dados ProjetosFrontEnd no servidor local, construído na plataforma SQL Server (SGBD open-source da Microsoft). A proposta do projeto é realizar uma integração entre a área de back-end e a área de front-end de modo que os endereços armazenados nesse ambiente sejam posteriormente utilizados para construção de um painel interativo pela equipe de desenvolvimento web.'
    ,docs_url='/documentacao'
    ,version='1.0.0'
    ,openapi_url='/armazenamentourls.json'
)
app.include_router(router=router_obj, tags=['APP Geral'])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, debug=True, reload=True)