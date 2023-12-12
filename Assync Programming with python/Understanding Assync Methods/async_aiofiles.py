import asyncio
import aiofiles

async def exemplo_arq1():
    async with aiofiles.open(r'C:\Users\LUCAS\Documents\Data Engineering\Data-Engineering\Assync Programming with python\texto.txt', 'r') as arquivo:
        conteudo = await arquivo.read()

    print(conteudo)
    
async def exemplo_arq2():
    async with aiofiles.open(r'C:\Users\LUCAS\Documents\Data Engineering\Data-Engineering\Assync Programming with python\texto.txt', 'r') as arq:
        async for linha in arq:
            print(linha.strip())

def main():
    el = asyncio.new_event_loop()
    asyncio.set_event_loop(el)

    el.run_until_complete(exemplo_arq2())

    el.close()

if __name__ == '__main__':
    main()