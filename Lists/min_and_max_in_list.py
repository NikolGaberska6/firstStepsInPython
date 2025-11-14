import sys
user_input = input("Въведете числа с интервал: ")

list = list(map(int, user_input.split()))
max = -sys.maxsize
min = sys.maxsize

for num in list:
    if num > max:
        max = num
    if num < min:
        min = num

print(f"Най-голямото число в листа е: {max}")
print(f"Най-малкото число в листа е: {min}")