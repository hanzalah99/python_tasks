import logging
import time
import asyncio

async def async_find_divisibles(in_range,divisor):
    start = time.time()
    log.info('find divisbles called with range %i and divisor %i',in_range,divisor)
    return_values = []
    for x in range(1,in_range+1):       #for loop is used for the range 2000-3200    
        if (x%divisor==0):      #if the number is divisble by and not divisible by 5
         return_values.append(x)
         await asyncio.sleep(0) 
    print(return_values)
    end = time.time()
    log.info('find divisbles ended with range %i and divisor %i. It took %f seconds',in_range,divisor,end-start)


  
log = logging.getLogger("my-logger")
level = logging.INFO
log.setLevel(level)
ch = logging.StreamHandler()
ch.setLevel(level)

log.addHandler(ch)



# Main driver code
ranges = [(50800000, 34113), (100052, 3210), (500, 3)]

async def run_tasks():
    tasks = []
    for number_range, divisor in ranges:
        tasks.append(async_find_divisibles(number_range, divisor))
    await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(run_tasks())
"""
async def tasks():
    async_find_divisibles(50800000,34113)
    async_find_divisibles(100052,3210)
    async_find_divisibles(500,3)
    await asyncio.gather(50800000,34113)
    await asyncio.gather(100052,3210)
    await asyncio.gather(500,3)
    
    
    
loop = asyncio.get_event_loop()
loop.run_until_complete(tasks())"""