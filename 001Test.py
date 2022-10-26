import time
from pyvscode_runner import pyVScodeRunner
import sys

@pyVScodeRunner
def main():
    print(f'Python version: {sys.version_info[0]}.{sys.version_info[1]}\n')
    for index in range(15):
        print(index)
        time.sleep(0.25)


if __name__ == '__main__':
    main()