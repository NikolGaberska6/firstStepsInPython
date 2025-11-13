import random

list = [random.randint(1, 20) for _ in range(20)]
print(f"Your list is: {list}")
dictionary = {}

for idx in list:
    dictionary[idx] = idx
    if idx % 2 == 0:
        dictionary[idx] = "even"
    else:
        dictionary[idx] = "odd"

print(dictionary)

