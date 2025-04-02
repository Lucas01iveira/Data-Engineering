import asyncio

async def compute_square(number):
    print(f'Initializing the compute of number {number}')
    await asyncio.sleep(number)
    print(f'The square of {number} is {number**2}')
    return number**2

async def main():
    numbers= [5,4,3,2,1]

    tasks= [
        asyncio.create_task(compute_square(i)) for i in numbers
    ]

    results= await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())

# -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- 
# 1) One important thing to notice is that even though the task list is being executed asynchronously, the code still attributes the correct answers into the results list according to each function result returned