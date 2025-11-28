numbers = input("Въведете числа за списъка: ")
list_of_numbers = list(map(int, numbers.split()))
list_of_positive_nums = []

for num in list_of_numbers:
    if num < 0:
        pass
    else:
        list_of_positive_nums.append(num)

print("Списъкът от положителни числа е : ", end=" ")
print(*list_of_positive_nums)