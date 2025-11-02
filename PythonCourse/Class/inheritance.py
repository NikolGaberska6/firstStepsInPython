

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):

    def speak(self):
        print("WOOF!")

class Cat(Animal):

    def speak(self):
        print("MEOW")

class Mouse(Animal):

    def speak(self):
        print("SQUEEK!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

dog.speak()

print(dog.name)     #if we print something from the UNIT function it always have "print"
print(dog.is_alive) #if we print something from the UNIT function it always have "print"
dog.eat()
cat.sleep()
mouse.eat()