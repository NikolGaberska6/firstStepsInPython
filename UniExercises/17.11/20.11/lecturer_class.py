from person_class import Person
from student_class import Student

class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        print (f"**************************\nName: {self.name} {self.family}\nNationality: {self.nationality}\n"
                f"University: {self.university}\nYear of experience: {self.experience}")
