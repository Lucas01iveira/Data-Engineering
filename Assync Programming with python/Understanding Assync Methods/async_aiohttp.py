import asyncio
import aiofiles
import aiohttp 
import bs4

# código construído em paralelo à aula e os critérios / explicações de aplicação dos comandos foi entendido perfeitamente, entretanto estamos impossibilitados de executar devido a um problema no download/instalação da biblioteca aiohttp (estamos recebendo um erro ao tentar instalar e não estamos encontrando em nenhum fórum a forma de corrigir esse erro)

# função que lê o arquivo de links e armazena numa lista
async def pegar_links():
    links = [] 
    async with aiofiles.open(r'C:\Users\LUCAS\Documents\Data Engineering\Data-Engineering\Assync Programming with python\links.txt', 'r') as arq:
        async for link in arq:
            links.append(link.strip())

    return links

# função que acessa um dado link e extrai o conteudo html da pagina
async def pegar_html(link):
    print('Pegando o html do curso {}'.format(link))

    async with aiohttp.ClientSesson() as session:
        async with session.get(link) as resp: # o get é um método http (referência biblioteca requests)
            resp.raise_for_status() # levanta qualquer tipo de erro que seja retornado durante a tentativa de acesso da pagina

            return await resp.text() # método para pegarmos o conteúdo da página (get do link acessado, nomeado como 'resp'), no formato texto
        
def pegar_titulo(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')

    title = soup.select_one('title') # pega o titulo da pagina

    title = title.text.split('|')[0].strip()


async def imprimir_titulos():
    links = await pegar_links()

    tarefas = []
    for link in links:
        tarefas.append(asyncio.create_task(pegar_html,link)) # gerando uma tarefa assincrona para cada chamada da função 'pegar_html' com base nos links diferentes

    for tarefa in tarefas:
        html = await tarefa

        title = pegar_titulo(html)

        print('Curso: {}'.format(title))
    
def main():
    el = asyncio.new_event_loop()
    asyncio.set_event_loop(el)

    el.run_until_complete(imprimir_titulos())

    el.close()
