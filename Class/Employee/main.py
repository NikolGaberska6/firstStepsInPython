from employee import Employee
from inheritance_employee import Manager

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