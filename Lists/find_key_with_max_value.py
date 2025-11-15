import sys

keys = input("Въведете думите, които искате да добавите като ключове: ").split()
values = input("Въведете числата, които искате да добавите като стойности: ").split()
max_num = -sys.maxsize

dictionary = {}
for key in keys:
    index = keys.index(key)
    value = values[index]
    dictionary[key] = value
    value = int(value)
    if value > max_num:
        max_num = value

needed_key = max_num
for key, value in dictionary.items():
    value = int(value)
    if value == needed_key:
     print(f"Ключа на най-голямата стойност е: {key}")
     break

