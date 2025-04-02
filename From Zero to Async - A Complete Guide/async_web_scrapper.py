import asyncio
import aiohttp

async def fetch_data(session, url):
    async with session.get(url) as response:
        print(f'Status for {url}: {response.status}')
        return response.text

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)
        
urls= [
    'https://python.org',
    'https://asyncio.readthedocs.io',
    'https://aiohttp.readthedocs.io'
]
asyncio.run(main(urls))