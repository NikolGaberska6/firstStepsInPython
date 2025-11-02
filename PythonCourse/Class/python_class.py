#object - bundle of related attributes (variables) and (methods)
#method - functions that belong to an object. They define what that object can do
#Class - needed to create many objects


class Car:                                                   #Class
    def __init__(self, model, year, color, for_sale):        #function
        #attributes that a car might have:
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):                                         #drive method
        print(f"You drive a {self.color} {self.model}")

    def stop(self):                                          #stop method
        print(f"You stop the {self.model}")

    def describe(self):                                      #describe method
        print(f"{self.year} {self.color} {self.model}")

car1 = Car("Mercedes", "1999", "white", True)
car2 = Car("Audi", "2006", "black", False)
car3 = Car("Volvo", "2006", "white", True)

car1.drive()
car2.stop()
car3.describe()


#print(car2.model)
#print(car2.year)
#print(car2.color)
#print(car2.for_sale)
