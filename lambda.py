# In Python, an anonymous function means that a function is without a name.
# As we already know that def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.
# template:
# lambda arguments: expression


double = lambda x: x * 2
print(double(5))


double = lambda x, y: x * y
print(double(5, 3))


# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print(new_list)


# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2, my_list))

print(new_list)
