from pathlib import Path
import sys
import os


# path to current file
# print(Path(sys.argv[0]).parts)

# get path extension
print(os.path.splitext(sys.argv[0]))
print(Path(sys.argv[0]).suffix)


print(os.path.splitdrive(Path(sys.argv[0])))
print(os.path.basename(Path(sys.argv[0])))


def format_paths():
    """
    correct way to deal with paths no matter of formatting
    """

    path = "C:\\Users\\nir\\Downloads\\generators.py"
    print(Path(path).parts)

    path = r"C:\Users\nir\Downloads\generators.py"
    print(Path(path).parts)

    path = "C:/Users/nir\Downloads\generators.py"
    print(Path(path).parts)

    path = "C:/Users//nir/Downloads/////\\\generators.py"
    print(Path(path).parts)
