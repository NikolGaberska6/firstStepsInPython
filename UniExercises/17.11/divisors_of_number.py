number = int(input("Въведете число: "))

for num in range(1, number + 1):
    if number % num == 0:
        print(num)