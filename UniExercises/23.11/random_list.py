import random

random_list = [random.randint(1, 10) for _ in range(1, 11)]
print(random_list)

average_sum = 0
num_of_numbers = 0
sum = 0
for num in random_list:
    num_of_numbers += 1
    sum += num

average_sum = sum / num_of_numbers
print(average_sum)

new_list = []
for number in random_list:
    if number > average_sum:
        new_list.append(number)
    else:
        pass

print(new_list)