class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def describe(self):
        print(f"The name of the employer is {self.name},"
              f" the position is - {self.position} and the "
              f"salary is - {self.salary}")

class Manager(Employee):
    def __init__(self, name, position, salary, team_size):
        super().__init__(name, position, salary)
        self.team_size = team_size

    def describe(self):
        print(f"Размера на екипа на {self.name} е: {self.team_size}")


employee1 = Employee("Mike", "IT", 5000)
employee2 = Employee("Ivan", "Cybersecurity engineer", 6000)
employee3 = Employee("Michael", "Assistant", 3000)

team_leader1 = Manager("Nikol", "Manager", 6000, 12)
team_leader2 = Manager("Ivan", "Manager", 7000, 34)
team_leader3 = Manager("Emo", "Manager", 7000, 34)

employee1.describe()
employee2.describe()
employee3.describe()
team_leader1.describe()
team_leader2.describe()
team_leader3.describe()