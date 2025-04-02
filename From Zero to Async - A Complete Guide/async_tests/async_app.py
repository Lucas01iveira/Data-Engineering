import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    return {'data': 123}