from fastapi import FastAPI # classe principal do módulo

app = FastAPI() 
# a partir do momento que eu gero o objeto (i.e., essa instância da classe FastAPI), ele se torna um 'decorator', que pode receber a atribuição dos métodos padrão (get, put, post, delete)


@app.get('/msg')
async def mensagem(): 
    return {'msg': 'FastApi na Geek University'}

# maneira de executar o código / a aplicação sem precisar usar o terminal
# (python -m uvicorn main:app --reload)
if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)
    # se mais pessoas com acesso à rede estiverem desenvolvendo a api em conjunto, devemos
    # trocar o host para 0.0.0.0 (desse modo, todos podem acessar)