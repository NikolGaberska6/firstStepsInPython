number = input("Въведете цяло число: ")
even_nums = []
odd_nums = []

for idx in number:
    idx = int(idx)
    if idx % 2 == 0:
        even_nums.append(idx)
    else:
        odd_nums.append(idx)

print("Листа с четните цифри на числото е: ")
print(*even_nums)
print("Листа с нечетните цифри на числото е: ")
print(*odd_nums)