user_list = input("Въведете числа за листа: ")
my_list = list(map(int, user_list.split()))

list_without_repeat = []

for num in my_list:
    if num in list_without_repeat:
        pass
    else:
        list_without_repeat.append(num)

print("Числата без повторенията са: ", end=" ")
print(*list_without_repeat)