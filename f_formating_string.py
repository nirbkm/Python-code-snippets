# https://docs.python.org/3/library/string.html#format-string-syntax


num = 11
print(f"num equal to: {num}")
print(f"num equal to: {num=}")  # add variable name and value
print(f"num equal to: {num:.5f}")  # adds fixed number of decimal locations


grade = 29 / 45
print(f"My grade rounded to 3 decimals is {grade:.3%}.")  # percentage
grade = 0.25
print(f"My grade rounded to 3 decimals is {grade:.3%}.")


bignumber = 100
print(f"I am worth {bignumber:,}$")  # comma seperator for big numbers

bignumber = 100000
print(f"I am worth {bignumber:,}$")  # comma seperator for big numbers
