import asyncio
import logging 
import time

#logging.basicConfig(level= logging.DEBUG, format= "'%(asctime)s %(levelname)s:%(message)s'")
logging.basicConfig(level= logging.DEBUG, format= "'%(asctime)s %(levelname)s:%(message)s'")

async def simulate_io_task(name, duration):
    logging.info(f'Task {name}: Starting with duration of {duration}')
    await asyncio.sleep(duration)
    logging.info(f'Task {name}: Completed')
    return duration 

async def main():
    start_time= time.perf_counter()
    # tasks with reverse time (good to see the true power of asyncio working)
    #tasks= [
    #    simulate_io_task(f'Task {i}', -i+4) for i in range(1,4)
    #]

    tasks= [
        simulate_io_task(f'Task {i}', i) for i in range(1,4)
    ]

    durations= await asyncio.gather(*tasks)

    total_duration= sum(durations)
    end_Time= time.perf_counter()

    logging.info(
        f'All tasks completed in {end_Time- start_time} seconds, total sleep duration was {total_duration} seconds'
    )

asyncio.run(main())