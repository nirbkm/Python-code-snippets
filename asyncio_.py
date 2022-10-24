import asyncio

# running in the same GIL ,
# best way to describe it as chess player that playing against several slower players,
# instead of finish one game and go to the other, the player doing one move for each oponnet, 
# this way job is being done faster.

# async - asynchronous - synchronous code is meant to running python script line by line by sequence, asynchronous is non siquencial.

# used for IO bound scripts (loading database,serial connection etc..) -> operation that are mostly waiting while PC is not really doing nothing in this time,
# for CPU bound scripts (adding thousends of values to list etc..) use multiprocessing which uses different GIL.

# keywords:
# await - hold - must be inside async function.
# async event loop - handles async operations. (async.run() etc..)
# async function -> courotine function/object, function that support asynchronous operation


async def main():
    print('nir')

# print(main()) # not running the main function but returns corutine

asyncio.run(main())