user_list = input("Въведете цели числа, разделени с интервал: ")
my_list = list(map(int, user_list.split()))

positive_nums = 0
negative_nums = 0
zero_nums = 0
list_of_positive_nums = []
list_of_negative_nums = []
list_of_zeros = []

for num in my_list:
    if num == 0:
        zero_nums +=1
        list_of_zeros.append(num)
    elif num < 0:
        negative_nums += 1
        list_of_negative_nums.append(num)
    elif num > 0:
        positive_nums += 1
        list_of_positive_nums.append(num)


print(f"Положителните числа са: {positive_nums} и те са: ", end=" ")
print(*list_of_positive_nums)
print(f"Отрицателните числа са: {negative_nums} и те са: ", end=" ")
print(*list_of_negative_nums)
print(f"Нулите са: {zero_nums} и те са: ", end=" ")
print(*list_of_zeros)