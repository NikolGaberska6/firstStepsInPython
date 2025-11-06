import sys
def biggest_number(num1, num2, num3):
    biggest_number = -sys.maxsize

    num_list = [num1, num2, num3]
    for num in num_list:
        if num > biggest_number:
            biggest_number = num
        else:
            continue

    return biggest_number


print(biggest_number(num1=int(input()), num2=int(input()), num3=int(input())))