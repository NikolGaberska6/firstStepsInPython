class Person:
    def __init__(self, name, family, age, nationality): #дефиниране на конструктур
        #инициализиране на полетата на класа:
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self): #създаване на метод print
        return f"**************************\nName: {self.name} {self.family}\nNationality: {self.nationality}"
