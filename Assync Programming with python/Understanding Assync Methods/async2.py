import datetime
import asyncio

async def gerar_dados(quantidade: int, dados: asyncio.Queue):
    print('Aguarde a geração de {} dados...'.format(quantidade))

    for idx in range(1, quantidade+1):
        item = idx+idx
        await dados.put((item, datetime.datetime.now()))
        #await asyncio.sleep(0.001)
    
    print(f'{quantidade} dados gerados com sucesso...')

async def processar_dados(quantidade: int, dados: asyncio.Queue):
    print('Aguarde o processamento de {} dados...'.format(quantidade))
    processados  = 0
    while processados < quantidade:
        await dados.get()
        processados +=1
        #await asyncio.sleep(0.0001)
    
    print('Foram processados {} itens.'.format(quantidade))

async def main():
    total = 5_000
    dados = asyncio.Queue()

    print('Computando {:.2f} dados'.format(total*2))

    await gerar_dados(total, dados)
    await gerar_dados(total, dados)
    await processar_dados(total*2, dados)

if __name__ == '__main__':
    el = asyncio.new_event_loop()
    asyncio.set_event_loop(el)
    
    el.run_until_complete(main())

    el.close()