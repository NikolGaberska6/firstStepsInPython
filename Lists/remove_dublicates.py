list_of_random = [1, 3, 4, 2, 4, 6, 4, 3]
print(list_of_random)

list_without_duplicates = []

for number in list_of_random:
        count = list_without_duplicates.count(number)
        if count >= 1:
            pass
        else:
            list_without_duplicates.append(number)

print(list_without_duplicates)