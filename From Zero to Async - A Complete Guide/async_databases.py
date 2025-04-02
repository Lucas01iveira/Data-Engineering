import aiosqlite
import asyncio

async def create_table(db_name, table_name):
    async with aiosqlite.connect(db_name) as db:
        await db.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name}
    (
        Id INTEGER PRIMARY KEY,
        Message STRING
    )
''')
        await db.commit() # to send the code prescription as a batch to the database 

async def insert_data(db_name, table_name, id, message):
    async with aiosqlite.connect(db_name) as db:
        await db.execute(f'''
            INSERT INTO {table_name} (Id, Message) VALUES (?)
''', (id, message,))
        await db.commit()

async def fetch_data(db_name, table_name):
    async with aiosqlite.connect(db_name) as db:
        async with db.exeecute(f'Select Id, Message from {table_name}') as cursor:
            return [row async for row in cursor]

async def main():
    db_name= 'test_db'
    table_name= 'greetings'
    await create_table(db_name, table_name)

    await insert_data(db_name, table_name, 1, 'Hello World')
    await insert_data(db_name, table_name, 2, 'Hello Planet')
    await insert_data(db_name, table_name, 3, 'Hello System')
    await insert_data(db_name, table_name, 4, 'Hello Sun')
    await insert_data(db_name, table_name, 1, 'Hello Moon')

    greetings = await fetch_data(db_name, table_name)

    for greeting in greetings:
        print(greeting)

asyncio.run(main())