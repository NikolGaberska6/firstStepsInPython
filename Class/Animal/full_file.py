class Animal:
    def __init__(self, species, age, sound): #дефиниране на конструктур
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self): #създаване на метод
        print(self.sound)

class Dog(Animal):
    def __init__(self, species, age, sound, breed):
        super().__init__(species, age, sound)
        self.breed = breed

    def make_sound(self):
        return f"Кучето от порода {self.breed} казва: Woof!"

#създаване на инстанции
cat = Animal("cat", 3, "Meow")
dog = Animal("dog", 4, "Woah")
fish = Animal("fish", 2, "Blue-blue")
Animal.make_sound(cat)
Animal.make_sound(dog)
Animal.make_sound(fish)

dog1 = Dog("Mike", 7, "Woof", "bulldog")
dog2 = Dog("Maks", 8, "Woof", "poodle")
dog3 = Dog("Toby", 9, "Woof", "chihuahua")
#aко е с return
print(Dog.make_sound(dog1))
print(Dog.make_sound(dog2))
print(Dog.make_sound(dog3))
#ако е с print
# dog1.make_sound()
# dog2.make_sound()
# dog3.make_sound()