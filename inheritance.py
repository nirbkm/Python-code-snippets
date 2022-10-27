class Car:
    def __init__(self, brand, year, color) -> None:
        self.brand = brand
        self.year = year
        self.color = color

    def getCarDetails(self):
        print(f"Brand: {self.brand}, Year: {self.year}, Color: {self.color}")

    def getCarBrand(self):
        print(f"Brand: {self.brand}")

    def __str__(self):
        return "This "


class subCar(Car):
    def getCarDetails(self):  # overide function
        print(
            f"Brand_sub: {self.brand}, Year_sub: {self.year}, Color_sub: {self.color}"
        )


c = Car("mazda", 2019, "grey")
c.getCarDetails()

cSub = subCar("suzuki", 2014, "gray")
cSub.getCarBrand()
cSub.getCarDetails()

print(c)
print(cSub)
