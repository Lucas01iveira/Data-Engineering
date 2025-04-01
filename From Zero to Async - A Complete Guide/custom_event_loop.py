import asyncio

async def task(name, delay):
    print(f'Task {name} starting with delay of {delay}')
    await asyncio.sleep(delay)
    print(f'Task {name} finished.')
    return f"Task {name} result"

async def main():
    tasks= [
        task(i,j) for i,j in zip(("A","B","C"), (3,2,1))  
    ]

    results= await asyncio.gather(*tasks) # to run them concurrently

    # after all tasks are completed, the main functions prints our results
    # (here yes, in the same order functions were called)
    for result in results:
        print(result)

asyncio.run(main())

# -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- ]
# Here we have one very common case of application of the async lib.

# Having defined our async coroutine, the main function groups our tasks into a list in order to execute all of them below the management of the event loop (with the help of async gather). The '*' means we are applyng the function to all the list items individually (not the list itself)

# In the end, after all the tasks were executed asynchronously, we print the results in the appropriate order (without any new feature)