user_nums = input("Въведете числа за списък: ")
my_list = list(map(int, user_nums.split()))

result = list(filter(lambda x: x > 10, my_list))
print("Числата по-големи от 10 са: ", end="")
print(*result)