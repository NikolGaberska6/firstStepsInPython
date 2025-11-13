def sum_of_nums(list):
    sum = 0
    for idx in list:
        if idx == " ":
            continue
        else:
         idx = int(idx)
         sum += idx

    return sum

list = input()
print(sum_of_nums(list))