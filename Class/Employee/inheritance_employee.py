from employee import Employee

class Manager(Employee):
    def __init__(self, name, position, salary, team_size):
        super().__init__(name, position, salary)
        self.team_size = team_size

    def describe(self):
        print(f"Размера на екипа на {self.name} е: {self.team_size}")