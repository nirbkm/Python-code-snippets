from functools import wraps
import time
import logging

def pyVScodeRunner(orig_func):
    logging.basicConfig(
         level=logging.INFO, 
         format= '\033[93m[%(asctime)s] - %(message)s\033[0m\n',
         datefmt='%H:%M:%S'
     )

    @wraps(orig_func)# not mandatory here, added in the 'based on' video only when chaining(applying) two decorations on the same function to save original function name and idenity, probably best to try without this decorator first and see if works
    def wrapper(*args, **kwargs): # get data from orig_func
        logging.info('Started Code Run')
        t1 = time.perf_counter()
        result = orig_func(*args, **kwargs)
        print('\n')
        logging.info(f'[ {orig_func.__name__} ] ran in: {time.perf_counter() - t1:.5f} sec\n')

        return result

    return wrapper


# import time
# from pyvscode_runner import pyVScodeRunner


# @pyVScodeRunner
# def main():
#     for index in range(15):
#         print(index)
#         time.sleep(0.25)


# if __name__ == '__main__':
#     main()