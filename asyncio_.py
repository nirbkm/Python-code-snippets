import asyncio
import time
#import sys

#print(sys.prefix)

# https://docs.python.org/3/library/asyncio-api-index.html

# running in the same GIL ,
# best way to describe it as chess player that playing against several slower players,
# instead of finish one game and go to the other, the player doing one move for each oponnet, 
# this way job is being done faster.

# again - only one thing happen at certain time, always. it just that when PC waits to some IO operation that he doesnt really do nothing else at the time, you can program it to do something else till finish.

# async - asynchronous - synchronous code is meant to running python script line by line by sequence, asynchronous is non siquencial.

# used for IO bound scripts (loading database,serial connection etc..) -> operation that are mostly waiting while PC is not really doing nothing in this time,
# for CPU bound scripts (adding thousends of values to list etc..) use multiprocessing which uses different GIL.

# keywords:
# await - hold(free translation)- blocking!! -runs asyncio def function(coroutine) -  must be inside async function.
    # -  The await keyword suspends execution of a coroutine until it completes and returns the result data, this keyword is what allows the couroutine to know it can do something else until the await returns !!
# async event loop - handles async operations. (async.run() etc..)
# asyncio.create task is running the coroutine in asynchronous way, part of the event loop
# async function -> courotine function/object, function that support asynchronous operation

###############
## example 1 ##
###############

async def fetchData():
    print('start fetching')
    await asyncio.sleep(2) # await keyword waits until line completes (i.e read from DB, http request etc..), but let python know it can do something else in between.
    # time.sleep(2) # this will block the code as no await keyword is here to let pyton know it can do something else this time.
    print('done fetching')
    return {'data':1}

async def printNumbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)
        
async def main():
    task1 = asyncio.create_task(fetchData())
    task2 = asyncio.create_task(printNumbers())

    value = await task1
    print(value)

    await task2

asyncio.run(main())

###############
## example 2 ##
###############
async def main():
    print('nir')
    # await foo('this is the text') # blocking run
    task = asyncio.create_task(foo('this is the text'))
    await task # wait until it finish, the task object will save the return value from foo function.
    print('finished main function')

async def foo(text):
    print(text)
    await asyncio.sleep(2)

# print(main()) # not running the main function but returns corutine

#asyncio.run(main())