class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
         return f"The brand is {self.brand}, the model is {self.model} and the year is {self.year}."