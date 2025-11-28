from person_class import Person

class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy

    def print(self):
        return f"\nUniversity: {self.university}\nYear of study: {self.yearofstudy}"