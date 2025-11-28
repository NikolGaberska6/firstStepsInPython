numbers = input("Въведете числа за списъка: ")
list_of_numbers = list(map(int, numbers.split()))

sorted_list = sorted(list_of_numbers, reverse=True)
print("Листа от числа, подредени в низходящ ред е: ", end=" ")
print(*sorted_list)