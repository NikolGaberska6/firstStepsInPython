doc1_keys = input("Въведете думите, които искате да добавите като ключове: ")
doc2_values = input("Въведете числата, които искате да добавите като стойности: ")
list1 = list(map(str, doc1_keys.split()))
list2 = list(map(int, doc2_values.split()))

dictionary1 = {}
for key in list1:
    index = list1.index(key)
    value = list2[index]
    dictionary1[key] = value
print("Първият речник е: ")
print(dictionary1)

doc2_keys = input("Въведете думите, които искате да добавите като ключове: ")
doc2_values = input("Въведете числата, които искате да добавите като стойности: ")
list_1 = list(map(str, doc2_keys.split()))
list_2 = list(map(int, doc2_values.split()))

dictionary2 = {}
for key_1 in list_1:
    index = list_1.index(key_1)
    value = list_2[index]
    dictionary2[key_1] = value
print("Вторият речник е: ")
print(dictionary2)

merged = {}
for key, value in dictionary1.items(): #merged items from dictionary1
    merged[key] = value

for key, value in dictionary2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value

print("Обединеният речник е: ")
print(merged)
