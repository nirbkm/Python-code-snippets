# Decorators
from functools import wraps
import time
from pathlib import Path
import sys

from logger import Logger


#based on: https://youtu.be/FsAPt_9Bf3U

#decoration functions (or class) are used to add extra functionality to existing function, for example logging about running the function, timing the function etc.. 
# not have to be functionality thats examine overall function but also manipulating / taking advantage on function inputs as the wrapper decoration function get the inputs as args and kwargs

def my_logger(orig_func):

    log = Logger(logFileName='test', loggerName=Path(sys.argv[0]).parts[-1], loggingLevel='DEBUG')

    @wraps(orig_func)# not mandatory here, added in the 'based on' video only when chaining(applying) two decorations on the same function to save original function name and idenity, probably best to try without this decorator first and see if works
    def wrapper(*args, **kwargs):
        log.logger.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time ## add here general params

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        result = orig_func(*args, **kwargs)
        t2 = time.perf_counter() - t1
        print(f'{orig_func.__name__} ran in: {t2} sec')
        return result

    return wrapper




@my_timer
@my_logger
def display_info(name, age, fname):
   time.sleep(1)
   pass
   #print('display_info ran with arguments ({}, {})'.format(name, age))


#display_info('Tom', 22, fname = '111')

##############################
## decorator with arguments ##
##############################

# https://www.artima.com/weblogs/viewpost.jsp?thread=240845#decorator-functions-with-decorator-arguments

def decoratorFunctionWithArguments(arg1, arg2, arg3):
    def wrap(f):
        print("Inside wrap()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f
    return wrap

@decoratorFunctionWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

#print("After decoration")
#
#print("Preparing to call sayHello()")
#sayHello("say", "hello", "argument", "list")
#print("after first sayHello() call")
#sayHello("a", "different", "set of", "arguments")
#print("after second sayHello() call")


###############################

# def pyVScodeRunnerWithArguments(terminalColor):
    # print(terminalColor)
    # logging.basicConfig(
        #  level=logging.INFO, 
        #  format= '\033[35m[%(asctime)s] - %(message)s\033[0m',
        #  datefmt='%H:%M:%S'
    #  )
    # def wrap(f):
        # def wrapped_f(*args):
            # logging.info('Started Code Run')
            # t1 = time.perf_counter()
            # # print("Decorator arguments:", terminalColor), print(args)
            # result = f(*args)
            # logging.info(f'[ {f.__name__} ] ran in: {time.perf_counter() - t1:.5f} sec')
            # return result
        # return wrapped_f
    # return wrap
# 
# 
# @pyVScodeRunnerWithArguments('red')
# def helloWorld(data):
    # print('hello world running')
    # time.sleep(3)
    # print('second hellp')
# 
# 
# if __name__ == '__main__':
    # helloWorld('this is the data')


