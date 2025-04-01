import asyncio 
from datetime import datetime

async def say_after(time, what):
    await asyncio.sleep(time)
    print(what)

# main function
async def process():
    start= datetime.now()
    print('Started time: {}'.format(start))

    await say_after(3, 'Hello asyncIO')
    await say_after(1, 'Asyncio is a very powerful tool')

    end= datetime.now()
    print('Finish time: {}'.format(end))
    print('Total time taken: {}s'.format((end-start).seconds))


asyncio.run(process())

# -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- 
# 1) The 'async def' creates the asynchronous function (or coroutine) to be executed which can be paused and/or resumed by the event_loop 

# 2) The 'await' operator is used to wait the execution of the asynchronous operation/function

# 3) The 'asyncio.run' structure must always be used when we're dealing with such functions because it already handles the cretion and management of the event loop involving the functions

# 4) An event loop is a programming construct that continuously monitors and processes events from various sources. such as user input, network requests or timer events. It acts as a central hub that dispatches these events to the appropriate event handlers or callbacks
    # It is the event loop who has the responsability to manage the multitasks asynchronous execution

# Extra: it's fair to say that the way the above code was written the commands will be executed in the right order with no mistery! Just because we're dealing with async functions, it doesn't mean the execution will always be async. This kind of syntax is useful because it serves as a way to build the complementar routines (individual tasks that shall be executed for different varying parameters). However, the asynchronous execution itself will only occur when we gather the tasks into an asyncio object as we'll see later on.