import asyncio

async def diz_oi():
    print('Oi...')

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop() 

    # a execução desse script funciona, mas retorna o seguinte warning: 
    # DeprecationWarning: There is no current event loop

    # esse warning aparece sempre que tentamos chamar o método get_event_loop() do módulo asyncio sem ter um event loop já em execução (funcionalidade que passou a ter vigência a partir do python 3.11)

    # o código corrotinas2 apresenta uma maneira de corrigir esse problema para as versões mais atualizadas do Python

    event_loop.run_until_complete(diz_oi())
    event_loop.close()