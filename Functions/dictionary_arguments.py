def my_person(person):
    print(f"This is {person["Name"]}")
    print(f"He is {person["Age"]} years old")

#person = ({"Name":"Emil", "Age":27})
person =({"Name":input(), "Age":int(input())}) #dictionary
my_person(person)