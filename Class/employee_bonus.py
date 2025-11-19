class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def give_bonus(self, amount):
        self.pay += amount

employee_1 = Employee("Nikol", "Gaberska", 100)
employee_2 = Employee("Leq", "Nikolaeva", 400)
employee_3 = Employee("Alexandra", "Andonowa", 600)

employee_2.give_bonus(50)

print(employee_2.full_name(), employee_2.pay)
print(employee_1.pay)
print(employee_3.pay)
