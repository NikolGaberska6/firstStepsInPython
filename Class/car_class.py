class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_model(self):
        return f"{self.brand}, {self.model}, {self.year}"

car1 = Car("Audi", "A4", "2006")
car2 = Car("BMW", "X5", "2010")
car3 = Car("Mercedes", "C180", "2008")

print(car1.car_model())
print(car2.car_model())
print(car3.car_model())