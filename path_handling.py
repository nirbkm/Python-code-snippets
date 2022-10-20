from pathlib import Path
import sys

#path to current file
print(Path(sys.argv[0]).parts)

#correct way to deal with paths no matter of formatting

path = 'C:\\Users\\nir\\Downloads\\generators.py'

print(Path(path).parts)

path = r'C:\Users\nir\Downloads\generators.py'

print(Path(path).parts)

path = 'C:/Users/nir\Downloads\generators.py'

print(Path(path).parts)

path = 'C:/Users//nir/Downloads/////\\\generators.py'

print(Path(path).parts)