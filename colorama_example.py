from colorama import init, Fore, Back, Style
from functools import wraps


def my_timer(orig_func):
    import time  ## add here general params

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        result = orig_func(*args, **kwargs)
        t2 = time.perf_counter() - t1
        print(f"{orig_func.__name__} ran in: {t2} sec")
        return result

    return wrapper


@my_timer
def test_speed():

    for i in range(
        1_000
    ):  # speed different only applied to thousends of loop, very small gap (on 10_000 iteration difference of 2 seconds)
        print(Fore.RED + "Welcome to LinuxHint")
        # print('somered text')


init()
test_speed()
