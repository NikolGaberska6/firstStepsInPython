user_list = input("Въведете числа разделени с интервал: ")
my_list = list(map(int, user_list.split()))

first_num = my_list[0]
last_num = my_list[-1] 
my_list.remove(first_num)
my_list.insert(0, last_num)
my_list.pop(-1) #премахване на елемент на даден индекс (в случая на -1)
my_list.append(first_num)

print(my_list)
