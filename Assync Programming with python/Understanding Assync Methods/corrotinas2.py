import asyncio

async def diz_oi_demorado():
    print('Oi...')
    await asyncio.sleep(2) # toda função assincrona que formos executar dentro de um async def precisa receber o await 
    print('Todos...')

if __name__ == '__main__':
    event_loop = asyncio.new_event_loop() # inicializando o event loop
    asyncio.set_event_loop(event_loop) # confgurando o event loop para a thread OS vigente;
    event_loop.run_until_complete(diz_oi_demorado()) # sinalização de execução da função
    event_loop.close() # encerramento do event loop