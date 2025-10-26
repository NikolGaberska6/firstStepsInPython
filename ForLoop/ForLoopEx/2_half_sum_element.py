import sys
n = int(input())
max_number = -sys.maxsize
sum = 0

for idx in range(n):
    new_number = int(input())
    sum +=new_number
    if new_number > max_number:
        max_number = new_number

final_sum = sum - max_number
if final_sum == max_number:
    print(f"Yes\nSum = {final_sum}")
else:
    diff = abs(final_sum - max_number)
    print(f"No\nDiff = {diff}")