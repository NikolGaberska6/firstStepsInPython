user_nums = input("Въведете няколко числа: ")
my_list = list(map(int, user_nums.split()))
sum_of_digits = 0
dictionary = {}

for num in my_list: #535
    for idx in str(num):
        idx = int(idx)
        sum_of_digits += idx
        dictionary[num] = sum_of_digits

values = dictionary.values()

print(f"Числата са: ")
print(*dictionary.keys())
print("Cбора на цифрите им е: ")
print(*dictionary.values())