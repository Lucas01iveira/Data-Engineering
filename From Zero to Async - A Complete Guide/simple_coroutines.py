import asyncio

async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f'Hello {name}, after {delay} seconds')

async def main():
    # -- x -- 
    # task1= greet('Lucas', 1)
    # task2= greet('Maria', 2)

    # await task1
    # await task2
    # -- x -- 

    # with the above structure, we do not gain anything; it's just like a sync routine but written with the async sofistication;

    # now, if we define tasks properly, they will be scheduled inside the event loop execution and them the code will run asynchronously as we want (according, of course, to the parameters)

    task1= asyncio.create_task(greet('Lucas', 2))
    task2= asyncio.create_task(greet('Maria', 1))

    await task1
    await task2

    # (similar to what await asyncio.gather does, but in a more controled situation, with less items)
asyncio.run(main())