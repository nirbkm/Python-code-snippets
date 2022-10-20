

#The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.


def myfunc(n):
      return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry1'))
lst = list(x)
print(lst)


def myfunc(a, b):
      return f"{a} - {b}"

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
lst = list(x)
lst = tuple(x)
print(lst)