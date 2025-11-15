keys = input("Въведете думите, които искате да добавите като ключове: ")
value = input("Въведете числата, които искате да добавите като стойности: ")
dictionary = {}

list_of_keys = list(map(str, keys.split()))
list_of_values = list(map(int, value.split()))

for key in list_of_keys:
    index = list_of_keys.index(key)
    value_of_second_list = list_of_values[index]
    dictionary[key] = value_of_second_list

print("Вашият речник е:")
print(dictionary)

reversed_dict = {}
for key, value in dictionary.items():
    reversed_dict[value] = key

print("Вашият обърнат речник е: ")
print(reversed_dict)