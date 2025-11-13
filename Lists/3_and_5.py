number = int(input("Въведете цяло число: "))

list1 = []
list2 = []
for num in range(1, number):
    list1.append(num)
    if num % 3 == 0 or num % 5 == 0:
        list2.append(num)

print(list1)
print(list2)