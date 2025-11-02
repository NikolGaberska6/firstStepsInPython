
class Student:

    class_graduating_year = 2024             #Class variable - same for all
    num_students = 0

    def __init__(self, name, age):
        self.name = name                     #instant variable - unique for everyone
        self.age = age                       #instant variable - unique for everyone
        Student.num_students += 1

student1 = Student("John", 20)
student2 = Student("Michael", 22)
student3 = Student("Ivan", 25)
student4 = Student("Andy", 27)

print(f"My graduating class of {Student.class_graduating_year} "
      f" has {Student.num_students} students!")


print(Student.num_students)                   #print how many student we wrote: in this case - 3

print(student1.name)
print(student1.age)
print(Student.class_graduating_year)         #access a Class variable by the Class name: "Student."