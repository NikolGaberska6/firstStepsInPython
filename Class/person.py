class Person:
    def __init__(self, name, years):
        self.name = name
        self.years = years

class Teacher(Person):
    def __init__(self, name, years, subject):
        super().__init__(name, years)
        self.subject = subject

    def introduce(self):
        print(f'Аз съм {self.name}, преподавам {self.subject}.')

teacher1 = Teacher("Александър", 34, "литература")
teacher2 = Teacher("Иван", 24, "история")
teacher3 = Teacher("Благой", 28, "музика")
teacher1.introduce(), teacher2.introduce(), teacher3.introduce()