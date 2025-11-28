number = int(input("Въведете число: "))
even_list = []
num_deliters = 0
for num in range(1, number+1):
    if number % num == 0:
        if num % 2 == 0:
            even_list.append(num)
            num_deliters+=1
        else:
            pass
    else:
        pass

if num_deliters == 0:
    print("Числото няма четни делители!")
else:
 print("Четните делители на числото са: ")
 print(*even_list)