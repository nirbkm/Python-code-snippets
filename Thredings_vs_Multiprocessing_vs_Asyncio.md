
Just the same as PyQT Multi-thread & QProcesses.

in multiprocessing you leverage multiple CPUs to distribute your calculations. Since each of the CPUs runs in parallel, you're effectively able to run multiple tasks simultaneously. You would want to use multiprocessing for CPU-bound tasks. An example would be trying to calculate a sum of all elements of a huge list. If your machine has 8 cores, you can "cut" the list into 8 smaller lists and calculate the sum of each of those lists separately on separate core and then just add up those numbers. You'll get a ~8x speedup by doing that.

In (multi)threading you don't need multiple CPUs. Imagine a program that sends lots of HTTP requests to the web. If you used a single-threaded program, it would stop the execution (block) at each request, wait for a response, and then continue once received a response. The problem here is that your CPU isn't really doing work while waiting for some external server to do the job; it could have actually done some useful work in the meantime! The fix is to use threads - you can create many of them, each responsible for requesting some content from the web. The nice thing about threads is that, even if they run on one CPU, the CPU from time to time "freezes" the execution of one thread and jumps to executing the other one (it's called context switching and it happens constantly at non-deterministic intervals). So if your task is I/O bound - use threading.

asyncio is essentially threading where not the CPU but you, as a programmer (or actually your application), decide where and when does the context switch happen. In Python you use an await keyword to suspend the execution of your coroutine (defined using async keyword).

--- 
TL;DR

Making the Right Choice:

We have walked through the most popular forms of concurrency. But the question remains - when should choose which one? It really depends on the use cases. From my experience (and reading), I tend to follow this pseudo code:

`if io_bound:

    if io_very_slow:
        print("Use Asyncio")
    else:
        print("Use Threads")
else:
    print("Multi Processing")
`
CPU Bound => Multi Processing
I/O Bound, Fast I/O, Limited Number of Connections => Multi Threading
I/O Bound, Slow I/O, Many connections => Asyncio


---

There are several different libraries at play:

- threading: interface to OS-level threads. Note that CPU-bound work is - mostly serialized by the GIL, so don't expect threading to speed up - calculations. Use it when you need to invoke blocking APIs in - parallel, and when you require precise control over thread creation. - Avoid creating too many threads (e.g. thousands), as they are not - free. If possible, don't create threads yourself, use concurrent.- futures instead.


- multiprocessing: interface to spawning multiple python processes with - an API intentionally similar to threading. Multiple processes work in - parallel, so you can actually speed up calculations using this - method. The disadvantage is that you can't share in-memory - datastructures without using multi-processing specific tools.


- concurrent.futures: A modern interface to threading and - multiprocessing, which provides convenient thread/process pools it - calls executors. The pool's main entry point is the submit method - which returns a handle that you can test for completion or wait for - its result. Getting the result gives you the return value of the - submitted function and correctly propagates raised exceptions (if - any), which would be tedious to do with threading. concurrent.futures - should be the tool of choice when considering thread or process based - parallelism.


- asyncio: While the previous options are "async" in the sense that - they provide non-blocking APIs (this is what methods like apply_async - refer to), they are still relying on thread/process pools to do their - magic, and cannot really do more things in parallel than they have - workers in the pool. Asyncio is different: it uses a single thread of - execution and async system calls across the board. It has no blocking - calls at all, the only blocking part being the asyncio.run() entry - point. Asyncio code is typically written using coroutines, which use - await to suspend until something interesting happens. (Suspending is - different than blocking in that it allows the event loop thread to - continue to other things while you're waiting.) It has many - advantages compared to thread-based solutions, such as being able to - spawn thousands of cheap "tasks" without bogging down the system, and - being able to cancel tasks or easily wait for multiple things at - once. Asyncio should be the tool of choice for servers and for - clients connecting to multiple servers.


- When choosing between asyncio and multithreading/multiprocessing, - consider the adage that "threading is for working in parallel, and - async is for waiting in parallel".


- Also note that asyncio can await functions executed in thread or - process pools provided by concurrent.futures, so it can serve as glue - between all those different models. This is part of the reason why - asyncio is often used to build new library infrastructure.

---

# Multiprocessing

## Pros

- Separate memory space
- Code is usually straightforward
- Takes advantage of multiple CPUs & cores
- Avoids GIL limitations for cPython
- Eliminates most needs for synchronization primitives unless if you use shared memory (instead, - it's more of a communication model for IPC)
- Child processes are interruptible/killable
- Python multiprocessing module includes useful abstractions with an interface much like threading.Thread
- A must with cPython for CPU-bound processing

## Cons

- IPC a little more complicated with more overhead (communication model vs. shared memory/objects)
- Larger memory footprint

# Threading

## Pros

- Lightweight - low memory footprint
- Shared memory - makes access to state from another context easier
- Allows you to easily make responsive UIs
- cPython C extension modules that properly release the GIL will run in parallel
- Great option for I/O-bound applications

## Cons
- cPython - subject to the GIL
- Not interruptible/killable
- If not following a command queue/message pump model (using the Queue module), then manual use of - synchronization primitives become a necessity (decisions are needed for the granularity of - locking)
- Code is usually harder to understand and to get right - the potential for race conditions - increases dramatically

--- 

The threading module uses threads, the multiprocessing module uses processes. The difference is that threads run in the same memory space, while processes have separate memory. This makes it a bit harder to share objects between processes with multiprocessing. Since threads use the same memory, precautions have to be taken or two threads will write to the same memory at the same time. This is what the global interpreter lock is for.

Spawning processes is a bit slower than spawning threads.

---

Threading's job is to enable applications to be responsive. Suppose you have a database connection and you need to respond to user input. Without threading, if the database connection is busy the application will not be able to respond to the user. By splitting off the database connection into a separate thread you can make the application more responsive. Also because both threads are in the same process, they can access the same data structures - good performance, plus a flexible software design.

Note that due to the GIL the app isn't actually doing two things at once, but what we've done is put the resource lock on the database into a separate thread so that CPU time can be switched between it and the user interaction. CPU time gets rationed out between the threads.

Multiprocessing is for times when you really do want more than one thing to be done at any given time. Suppose your application needs to connect to 6 databases and perform a complex matrix transformation on each dataset. Putting each job in a separate thread might help a little because when one connection is idle another one could get some CPU time, but the processing would not be done in parallel because the GIL means that you're only ever using the resources of one CPU. By putting each job in a Multiprocessing process, each can run on it's own CPU and run at full efficiency.