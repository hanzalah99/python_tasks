import logging
import time

def find_divisibles(in_range,divisor):
    start = time.time()
    log.info('find divisbles called with range %i and divisor %i',in_range,divisor)
    return_values = []
    for x in range(1,in_range+1):       #for loop is used for the range 2000-3200    
        if (x%divisor==0):      #if the number is divisble by and not divisible by 5
         return_values.append(x) 
    print(return_values)
    end = time.time()
    log.info('find divisbles ended with range %i and divisor %i. It took %f seconds',in_range,divisor,end-start)


  
log = logging.getLogger("my-logger")
level = logging.INFO
log.setLevel(level)
ch = logging.StreamHandler()
ch.setLevel(level)

log.addHandler(ch)


find_divisibles(50800000,34113)
find_divisibles(100052,3210)
find_divisibles(500,3)

