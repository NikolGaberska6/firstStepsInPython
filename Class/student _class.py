class Student:
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


student_1 = Student("Alexandra", "Andonova", 4)
student_2 = Student("Nikol", "Gaberska", 5)
student_3 = Student("Dara", "Gaberska", 6)

print(student_1.full_name())
print(f"Оценка на втория ученик: {student_2.grade}")
print(f"Пълното име на третия студент: {student_3.full_name()}")
print(f"Оценката на третия студент: {student_3.grade}")