from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def info(self):
        return f"The fuel type is {self.fuel_type}"