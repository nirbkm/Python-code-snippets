from dataclasses import dataclass

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
