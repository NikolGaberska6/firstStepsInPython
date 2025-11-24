class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        print(sum(self.grades) / len(self.grades))

student1 = Student("Nikol", 18)
student2 = Student("Leq", 20)
student3 = Student("Alexandra", 19)
student4 = Student("Yordan", 22)

print("Средният успех на студентите е: ")
student1.add_grade(4), student2.add_grade(2), student3.add_grade(3), student4.add_grade(5)
student1.add_grade(3), student2.add_grade(5), student3.add_grade(3), student4.add_grade(6)
student1.add_grade(5), student2.add_grade(4), student3.add_grade(4), student4.add_grade(5)
student1.add_grade(4), student2.add_grade(4), student3.add_grade(4), student4.add_grade(5)
print(f"{student1.name}: ", end= " ")
student1.get_average(),
print(f"{student2.name}: ", end= " ")
student2.get_average(),
print(f"{student3.name}: ", end= " ")
student3.get_average(),
print(f"{student1.name}: ", end= " ")
student4.get_average()
