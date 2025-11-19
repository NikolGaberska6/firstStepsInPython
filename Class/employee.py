class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    def full_name(self):
         return f"{self.first_name} : {self.last_name}"

employee_1 = Employee("Nikol", "Gaberska", 500)
employee_2 = Employee("leq", "Nikolaeva", 400)
employee_3 = Employee("Alexandra", "Andonowa", 600)


print(Employee.full_name(employee_1))
print(employee_1.full_name()) #прави същото като горното
print(employee_1.first_name)
print(employee_2.last_name)
print(employee_3.pay)


