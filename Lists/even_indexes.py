nums = input("Въведете числа: ")
list_of_nums = list(nums)
print(list_of_nums)

list_with_even_indexes = []

for num in list_of_nums:
     index = list_of_nums.index(num)
     if index % 2 == 0:
        list_with_even_indexes.append(num)

print(list_with_even_indexes)