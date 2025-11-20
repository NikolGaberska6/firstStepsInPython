from animal import Animal

class Dog(Animal):
    def __init__(self, species, age, sound, breed):
        super().__init__(species, age, sound)
        self.breed = breed

    def make_sound(self):
        return f"Кучето от порода {self.breed} казва: Woof!"

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