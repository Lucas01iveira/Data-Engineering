import asyncio
import time

# simulating a sync block operation (which locks the loop, preventing other tasks from going on)
def sync_blocking_operation():
    time.sleep(2)
    return "Operation completed"

async def run_sync_in_thread():
    # this function serves as a wrapper for the synchronous running operations

    loop= asyncio.get_running_loop() # getting the event loop that is already running
    result= await loop.run_in_executor(None, sync_blocking_operation)
    
    # The run_in_executor method allows you to run synchronous (blocking) code in a separate thread or process to prevent it from blocking the event loop.

    # The None argument tells the event loop to use the default executor (which is typically a ThreadPoolExecutor).

    print(result)

# async def main():
#     await run_sync_in_thread()

#asyncio.run(main())

asyncio.run(run_sync_in_thread())