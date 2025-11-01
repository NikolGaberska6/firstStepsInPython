#List comprehension = A concise way to create a list in Python
#                     Compact and easier to create than traditional loops
#                     [expression for value in iterable if condition]


#FORMULA [expression for value in iterable if condition]

doubles = []
for x in range (1, 11):
    doubles.append(x * 2)
print(doubles)

#doubles = [expression for value in iterable if condition]
doubles = [x * 2 for x in range(1, 11)]
print(doubles)
triple = [x * 3 for x in range(1, 11)]
print(triple)
squares = [x * x for x in range(1, 11)]
print(squares)

fruits = ["apple", "banana", "cherry"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

numbers = [1, -2, 3, 4, -6, -8]
positive_nums = [num for num in numbers if num >= 0] #more focused on if condition than in the expression
print(positive_nums)
negative_nums = [num for num in numbers if num <0]
print(negative_nums)
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)

grades = [34, 45, 95, 27, 49, 85, 12, 43]
passing_grades = [grade for grade in grades if grade > 35]
print(passing_grades)