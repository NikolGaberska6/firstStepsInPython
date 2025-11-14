user_list = input("Въведете числа за лист с интервали: ")
my_list = list(map(int, user_list.split()))
is_true = True

for num in my_list:
    index = my_list.index(num)
    next_index = index + 1
    if next_index >= len(my_list):
        is_true = True
        break
    else:
     next_num = my_list[next_index]
     if next_num > num:
         is_true = True
         continue
     else:
         print("Няма нарастваща последователност!")
         is_true = False
         break

if is_true:
 print("Има нарастваща последователност!")
