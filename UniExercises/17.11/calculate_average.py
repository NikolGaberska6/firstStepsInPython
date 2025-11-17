numbers = input("Въведете числа за списъка: ")
list_of_numbers = list(map(int, numbers.split()))
sum = 0
count = 0

for num in list_of_numbers:
    count += 1
    sum += num

average_sum = sum / count
print(f"Средната стойност на числата е: {average_sum}")