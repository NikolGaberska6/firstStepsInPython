names = input("Въведете 5 имена: ")
list_of_names = list(map(str, names.split()))
numbers = input("Въведете 5 телефонни номера: ")
list_of_telephone_nums = list(map(str, numbers.split()))

# print(list_of_names)
# print(list_of_telephone_nums)

dictionary = {}

for name in list_of_names:
    index = list_of_names.index(name)
    telephone_num = list_of_telephone_nums[index]
    dictionary[name] = telephone_num

searched_name = input("Въведи името, чиито телефонен номер искаш да получиш: ")
telephone_number = dictionary.get(searched_name)

print(f"Телефонния номер, който търсите е: {telephone_number}")