import random

num_numbers = int(input("Изберете колко числа да съдържа списъка: "))
list_of_nums = [random.randint(1, 100) for _ in range(num_numbers)]

print(f"Това е твоят рандом лист {list_of_nums}")
average_sum_from_first_sum = 0
sum_of_nums = 0
for number in list_of_nums:
    number = int(number)
    sum_of_nums += number

num_numbers = int(num_numbers)
average_sum_from_first_sum = sum_of_nums / num_numbers
list2 = []

for num in list_of_nums:
    if num > average_sum_from_first_sum:
        list2.append(num)
    else:
        pass

print(list2)


