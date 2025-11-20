class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
         return f"The brand is {self.brand}, the model is {self.model} and the year is {self.year}."

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def info(self):
        return f"The fuel type is {self.fuel_type}"

car1 = Vehicle("Audi", "A4", 2006)
car2 = Vehicle("BMW", "X5", 2012)
car3 = Vehicle("Mercedes", "C180", 2008)

type_fuel = Car("Audi", "A4", 2006, "diesel")
type_fuel2 = Car("BMW", "X5", 2012, "gas")
type_fuel3 = Car("Mercedes", "C180", 2008, "benzin")

print(car1.info(), type_fuel.info())
print(car2.info(), type_fuel2.info())
print(car3.info(), type_fuel3.info())
