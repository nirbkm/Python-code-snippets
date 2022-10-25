import time
from pyvscode_runner import pyVScodeRunner


@pyVScodeRunner
def main():
    for index in range(15):
        print(index)
        time.sleep(0.25)


if __name__ == '__main__':
    main()