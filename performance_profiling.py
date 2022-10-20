from time import perf_counter
from sys import getsizeof
import psutil
from line_profiler import LineProfiler
import time
import random

from si_prefix import si_format

###############################################################################################
## Memory usage measurements - measure memory usage of individual relevant areas in the code ##
###############################################################################################

def example():
    #time.sleep(1)

    start = psutil.virtual_memory().used
    print(si_format(start, precision= 4))


    arr = [1] * 100_000_000

    #time.sleep(1)

    end = psutil.virtual_memory().used
    print(si_format(end, precision= 4))

    print(f"delta: {si_format(end-start, precision = 4)}")

    # also can measure size of array or any object directly with getsizeof
    print(si_format(getsizeof(arr), precision= 4))  

#example()

####################################################################################################
## CPU time measurements - accuratley measure processing time during script in relevant positions ##
#################################################################################################### 

def slow_function():
    time.sleep(7)
    arr = [random.randint(1,100) for i in range(100000)]
    return sum(arr) / len(arr)

def measure_time():
    start = perf_counter() # return time in seconds
    slow_function()
    stop = perf_counter()

    print(start, stop)
    print(stop-start)


#measure_time()



####################################################
## CPU time measurements - line by line profiling ## 
####################################################

# basically rely on process time, can be replaced by time.perf_counter() inside the script to monitor relevant areas in code

def very_slow_random_generator(data):
    print(data)
    time.sleep(5)
    arr = [random.randint(1,100) for i in range(100000)]
    return sum(arr) / len(arr)

def fast_random_generator(data):
    time.sleep(1)
    arr = [random.randint(1,100) for i in range(100000)]
    return sum(arr) / len(arr)

# single function #
def single_function_profiling():
    lp = LineProfiler()
    lp_wrapper = lp(very_slow_random_generator) # single function
    lp_wrapper('pass data from here')
    lp.print_stats()


# multiple functions #

# wrap tested function with some function
def main_func(data):
    result = fast_random_generator(data)
    print(result)

    result = very_slow_random_generator(data)
    print(result)


def multi_function_profiling():
    lp = LineProfiler()
    lp.add_function(very_slow_random_generator)
    lp.add_function(fast_random_generator)
    lp_wrapper = lp(main_func)
    lp_wrapper('pass data from here')
    lp.print_stats()


########################################################
## Memory usage measurements - line by line profiling ##
########################################################

from memory_profiler import profile

@profile(precision=4)
def my_func():
    #
    a = [1] * (10 ** 6)
    print(getsizeof(a)/1000) ## probably better as not entire program is needed to monitor memory, only large array most of the time, getsizeof is for bytes, /1000kb
    #b = [2] * (2 * 10 ** 7)
    #del b
    #return a

#my_func()