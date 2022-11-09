from dataclasses import dataclass

"""
# @classmethod is the way to call function not only as an instance of a class but also ***directly*** by the class itself as its first argument.
# The class method can only access the class attributes but not the instance attributes.

# @staticmethod is a way of putting a function into a class (because it logically belongs there), while indicating that it does not require access to the class (so we don't need to use self in function definition).
# It cannot access either class attributes or instance attributes.

# https://www.tutorialsteacher.com/python/classmethod-decorator
# https://stackoverflow.com/a/65754079


class DecoratorTest(object):
    factor = 1  # class attribute

    def __init__(self):
        self.instance_factor = 2  # instance attribute
        pass

    def doubler(self, x):
        return x * 2

    @classmethod
    def class_doubler(
        cls, x
    ):  # we need to use 'cls' instead of 'self'; 'cls' reference to the class instead of an instance of the class
        return (
            x * 2
        ) + cls.factor  # cannot accsses self.instance_factor, only cls.factor

    @staticmethod
    def static_doubler(
        x,
    ):  # no need adding 'self' here; static_doubler() could be just a function not inside the class
        return x * 2  # cannot accsses either self.instance_factor and cls.factor


decor = DecoratorTest()

print(decor.doubler(5))
print(
    DecoratorTest.doubler(5)
)  # cannot accses directly since doubler is not classmethod!!

print(decor.class_doubler(5))  # a call with an instance of a class
print(DecoratorTest.class_doubler(5))  # a direct call by the class itself

# staticmethod could be called in the same way as classmethod.
print(decor.static_doubler(5))  # as an instance of the class
print(DecoratorTest.static_doubler(5))  # or as a direct call
"""

"""
# property allows you to add getter and setter functionality over setting and getting values from function.
class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        # print("Getting value...")
        return f"Temperature is: {self._temperature}"

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value  # _temperature is special sign for privacy of val inside function, if you will set temperature directly it will call the setter again inifinte times, recusion


c = Celsius(100)

print(c.temperature)

c.temperature = -300
"""

"""
@dataclass(frozen=True, order=True)
class Animal:
    age: float
    name: str
    animal_type: str = "Anonymous"

    def __repr__(self) -> str:
        return (
            f"This class represents animal: {self.animal_type}, {self.age}, {self.name}"
        )


a = Animal(animal_type="Dog", age=20, name="Zoey")
b = Animal(animal_type="Dog", age=40, name="Zoey")
c = Animal(animal_type="Cat", age=10, name="Mitzi")

# print(a)
# print(b)

# print(a == b)
# print(a is b)

# print(a.age)

# lst = [a, b, c].sort()
# print(lst)


# dataclass frozen make class immutable so it can serve as a dict key
# new_dict = {a: "fdd"}
# print(new_dict)

# dataclass order make it possible to sort or do les then greater etc on the class
print(a > b)

k = lambda x: x.age

lst = [a, b, c]
lst.sort(key=k)
print(lst)
"""
