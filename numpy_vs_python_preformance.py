import numpy as np
from functools import wraps
from pyvscode_runner import pyVScodeRunner


ITERATIONS_NUMBER = 10_000


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
def python_array_append():
    data = [1]
    for x in range(ITERATIONS_NUMBER):
        avg = sum(data) / len(data)
        data.append(avg)


@my_timer
def numpy_array_append():
    data = np.array([1])
    for x in range(ITERATIONS_NUMBER):
        data = np.append(data, np.mean(data))


@pyVScodeRunner
def main():
    numpy_array_append()
    python_array_append()


if __name__ == "__main__":
    data: str = 1
    print(type(data))
    # main()
