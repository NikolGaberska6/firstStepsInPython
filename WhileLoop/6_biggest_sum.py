import sys
biggest_num = -sys.maxsize
number = input()

while number != "Stop":
    number = int(number)
    if number > biggest_num:
        biggest_num = number
    number = input()

print(biggest_num)
