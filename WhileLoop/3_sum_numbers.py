all_sum = int(input())
new_sum = 0
is_smaller = True

while is_smaller:
    new_num = int(input())
    new_sum += new_num
    if new_sum >= all_sum:
        print(new_sum)
        is_smaller = False
    else:
        continue

