n = int(input("Въведете число, до което искате да сумирате: "))
sum = 0

for num in range(2, n + 1):
    if num % 2 == 0:
       sum += num

print(sum)
