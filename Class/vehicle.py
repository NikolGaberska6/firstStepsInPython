class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__ (self, brand, model, year):
        super().__init__(brand, model)
        self.year = year
        self.mileage = 0

    def km(self, km):
        self.mileage += km

    def info(self):
        print(f"Марка: {self.brand}, модел {self.model}, година: {self.year}, километри: {self.mileage}")

car1 = Car("BMW", "X5", "2023")
car1.km(250), car1.info()
car2 = Car("Audi", "A3", "2025")
car2.km(160), car2.info()
car3 = Car("Mercedes", "C180", "2020")
car3.km(340), car3.info()
