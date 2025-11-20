class Person:
    def __init__(self, name, family, age, nationality): #дефиниране на конструктур
        #инициализиране на полетата на класа:
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self): #създаване на метод print
        return f"**************************\nName: {self.name} {self.family}\nNationality: {self.nationality}"

class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy

    def print(self):
        return f"\nUniversity: {self.university}\nYear of study: {self.yearofstudy}"

class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        print (f"**************************\nName: {self.name} {self.family}\nNationality: {self.nationality}\n"
                f"University: {self.university}\nYear of experience: {self.experience}")


#обекти инсталации за класа:
person1 = Student("Nikol", "Gaberska", 19, "Bulgarian", "TU", 1)
person2 = Student("Alexandra", "Andonova", 20, "Italian", "UNSS", 2)
person3 = Student("Petar", "Georgiev", 21, "American", "YASG", 3)

lecturer1 = Lecturer("Ivan", "Petrov", 25, "Bulgarian", "UASG", 3)
lecturer2 = Lecturer("Yoan", "Mihailov", 23, "Bulgarian", "TU", 4)
lecturer3 = Lecturer("Dimitur", "Georgiev", 30, "Bulgarian", "UNSS", 5)

#извикване на метода printx
print(Person.print(person1), Student.print(person1))
print(Person.print(person2), Student.print(person2))
print(Person.print(person3), Student.print(person3))
#ако е с print
lecturer1.print()
lecturer2.print()
lecturer3.print()
#ако е с return
# print(Lecturer.print(lecturer1))
# print(Lecturer.print(lecturer2))
# print(Lecturer.print(lecturer3))