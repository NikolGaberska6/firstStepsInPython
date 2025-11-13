number = input("Въведете едно цяло число: ")
even_list = []
odd_list = []

for idx in number:
    idx = int(idx)
    if idx % 2 == 0:
        even_list.append(idx)
    else:
        odd_list.append(idx)

print(even_list)
print(odd_list)
