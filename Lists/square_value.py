number = int(input("Въведете число: "))

dictionary = {}
for i in range(1, number+1):
    dictionary[i] = i * i

print(dictionary)
