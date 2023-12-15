import datetime
import math as m
import asyncio

def main():
    print('Realizando processamento de forma assíncrona...')
    
    el = asyncio.new_event_loop()
    asyncio.set_event_loop(el)

    inicio = datetime.datetime.now()

    el.run_until_complete(computar(inicio=1, fim=50_000_000)) # forma 1

    final = datetime.datetime.now()
    tempo_total = final-inicio

    print('O processamento levou um tempo total de {:.2f} s'.format(tempo_total.total_seconds()))

    el.close()

async def computar(fim, inicio=1):
    pos = inicio
    fator = 1000*1000
    await asyncio.sleep(0.001)
    while pos < fim:
        m.sqrt( (pos - fator)*(pos - fator) )
        pos += 1
        

if __name__ == '__main__':
    main()

# Tempo total gasto : 35.61