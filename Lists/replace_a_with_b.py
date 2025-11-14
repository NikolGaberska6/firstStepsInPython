from operator import index

user_list = input("Въведете числа с интервал: ")
my_list = list(map(int, user_list.split()))
a = int(input("Въведете числото а: "))
b = int(input("Въведете числото b: "))

for num in my_list:
    if num == a:
        idx = my_list.index(num)
        my_list.remove(a)
        my_list.insert(idx, b)
    else:
        pass

print(my_list)