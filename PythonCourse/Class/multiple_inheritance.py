#multiple inheritance = inherit from more than one parent Class
#                       C(A, B)
#multilevel inheritance = inherit from a parent which inherits from another parent
#                         C(B) <- B(A) <- A

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")

class Victims(Animal):
    def run (self):
        print(f"{self.name} animal is running")

class Hunters(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Victims):
    pass

class Hawk(Hunters):
    pass

class Fish(Victims, Hunters):
    pass

rabbit = Rabbit("Bunny")
hawk = Hawk("Tony")
fish = Fish("Nemo")

print(rabbit.name)
hawk.hunt()
fish.sleep()