# Magic or Dunder Methods - double underscore __init__ for exmp
# references:
# https://rszalski.github.io/magicmethods/
# https://www.tutorialsteacher.com/python/magic-methods-in-python


# check class magic methods:
# dir(class_name)


class addTwoNumbers(object):
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

        # print('init')

    def __str__(self):
        return f"This function adds up {self.a} with {self.b}"

    def __index__(
        self,
    ):  ## need for type conversion as hex, to return the number to convert, cant use __hex__ directly on class varialbles
        print("Index is being called")
        return self.a

    def __hex__(self, val):
        return hex(val)

    def __int__(self):
        return int(self.a)

    def __add__(self, other):
        return self.a + self.b + other

    def __getattribute__(
        self, attr
    ):  # calls each time attribute is being called (className.something)
        # print(f"__getattribute__ : {attr}") # custom funcionality
        return object.__getattribute__(
            self, attr
        )  # have to be here to maintain function functunality

    def __getattr__(
        self, attr
    ):  # calls when attribute is being called but not exist in the class
        # print(f'__getattr__ Attribute does not exist: {attr}')
        return None


t = addTwoNumbers(5, 10)

# print(str(t))
# print(repr(t))
print(hex(t))
print(int(t))

# x = t.does_not_exist
# print(f"x: {x}")
#
#
# print(f"Add: {t + 1}") # add


#####################
## Magic functions ##
#####################

# Dict and List does not implement __getitem__ the same way. Dict objects uses a comparison (__eq__) on __hash__ of objects as key to use in __getitem__.
# To make Thing usable for dict you have to implement both hash and eq.


# __new__(cls, other)	To get called in an object's instantiation.
# __init__(self, other)	To get called by the __new__ method.
# __del__(self)	Destructor method.

# Unary operators and functions	Description

# __pos__(self)	To get called for unary positive e.g. +someobject.
# __neg__(self)	To get called for unary negative e.g. -someobject.
# __abs__(self)	To get called by built-in abs() function.
# __invert__(self)	To get called for inversion using the ~ operator.
# __round__(self,n)	To get called by built-in round() function.
# __floor__(self)	To get called by built-in math.floor() function.
# __ceil__(self)	To get called by built-in math.ceil() function.
# __trunc__(self)	To get called by built-in math.trunc() function.

# Augmented Assignment	Description

# __iadd__(self, other)	To get called on addition with assignment e.g. a +=b.
# __isub__(self, other)	To get called on subtraction with assignment e.g. a -=b.
# __imul__(self, other)	To get called on multiplication with assignment e.g. a *=b.
# __ifloordiv__(self, other)	To get called on integer division with assignment e.g. a //=b.
# __idiv__(self, other)	To get called on division with assignment e.g. a /=b.
# __itruediv__(self, other)	To get called on true division with assignment
# __imod__(self, other)	To get called on modulo with assignment e.g. a%=b.
# __ipow__(self, other)	To get called on exponentswith assignment e.g. a **=b.
# __ilshift__(self, other)	To get called on left bitwise shift with assignment e.g. a<<=b.
# __irshift__(self, other)	To get called on right bitwise shift with assignment e.g. a >>=b.
# __iand__(self, other)	To get called on bitwise AND with assignment e.g. a&=b.
# __ior__(self, other)	To get called on bitwise OR with assignment e.g. a|=b.
# __ixor__(self, other)	To get called on bitwise XOR with assignment e.g. a ^=b.

# Type Conversion Magic Methods	Description

# __int__(self)	To get called by built-int int() method to convert a type to an int.
# __float__(self)	To get called by built-int float() method to convert a type to float.
# __complex__(self)	To get called by built-int complex() method to convert a type to complex.
# __oct__(self)	To get called by built-int oct() method to convert a type to octal.
# __hex__(self)	To get called by built-int hex() method to convert a type to hexadecimal.
# __index__(self)	To get called on type conversion to an int when the object is used in a slice expression.
# __trunc__(self)	To get called from math.trunc() method.

# String Magic Methods	Description

# __str__(self)	To get called by built-int str() method to return a string representation of a type.
# __repr__(self)	To get called by built-int repr() method to return a machine readable representation of a type.
# __unicode__(self)	To get called by built-int unicode() method to return an unicode string of a type.
# __format__(self, formatstr)	To get called by built-int string.format() method to return a new style of string.
# __hash__(self)	To get called by built-int hash() method to return an integer.
# __nonzero__(self)	To get called by built-int bool() method to return True or False.
# __dir__(self)	To get called by built-int dir() method to return a list of attributes of a class.
# __sizeof__(self)	To get called by built-int sys.getsizeof() method to return the size of an object.

# Attribute Magic Methods	Description

# __getattr__(self, name)	Is called when the accessing attribute of a class that does not exist.
# __getattribute__(self, name) Is called for each accsess of attribute no matter if exist or not.
# __setattr__(self, name, value)	Is called when assigning a value to the attribute of a class.
# __delattr__(self, name)	Is called when deleting an attribute of a class.

# Operator Magic Methods	Description

# __add__(self, other)	To get called on add operation using + operator
# __sub__(self, other)	To get called on subtraction operation using - operator.
# __mul__(self, other)	To get called on multiplication operation using * operator.
# __floordiv__(self, other)	To get called on floor division operation using // operator.
# __truediv__(self, other)	To get called on division operation using / operator.
# __mod__(self, other)	To get called on modulo operation using % operator.
# __pow__(self, other[, modulo])	To get called on calculating the power using ** operator.
# __lt__(self, other)	To get called on comparison using < operator.
# __le__(self, other)	To get called on comparison using <= operator.
# __eq__(self, other)	To get called on comparison using == operator.
# __ne__(self, other)	To get called on comparison using != operator.
# __ge__(self, other)	To get called on comparison using >= operator.
