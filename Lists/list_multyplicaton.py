import random
list_random_numbers = []
num_numbers = int(input("Колко числа искаш да има в списъка: "))
list_random_numbers = [random.randint(1, 100) for _ in range(num_numbers)]
print(list_random_numbers)

second_list = []

for num in list_random_numbers:
    index = list_random_numbers.index(num)
    if index == 0:
        pass
    else:
        if index == len(list_random_numbers) - 1:
          previous_number = list_random_numbers[index - 1]
          next_number = 1
          new_number = previous_number * next_number
        else:
         previous_number = list_random_numbers[index - 1]
         next_number = list_random_numbers[index + 1]
         new_number = previous_number * next_number
         second_list.append(new_number)

print(second_list)