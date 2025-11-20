class Animal:
    def __init__(self, species, age, sound): #дефиниране на конструктур
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self): #създаване на метод
        print(self.sound)

#създаване на инстанции
cat = Animal("cat", 3, "Meow")
dog = Animal("dog", 4, "Woah")
fish = Animal("fish", 2, "Blue-blue")

Animal.make_sound(cat)
Animal.make_sound(dog)
Animal.make_sound(fish)