class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def describe(self):
        print(f"The name of the employer is {self.name},"
              f" the position is - {self.position} and the "
              f"salary is - {self.salary}")