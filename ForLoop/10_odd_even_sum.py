num = int(input())
sum_even = 0
sum_odd = 0

for idx in range(num):
    number = int(input())
    if idx % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

if sum_odd == sum_even:
    print(f"Yes\nSum = {sum_even}")
else:
    diff = abs(sum_odd - sum_even)
    print(f"No\nDiff = {diff}")