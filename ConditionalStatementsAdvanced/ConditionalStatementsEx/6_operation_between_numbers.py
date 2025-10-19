num1 = int(input())
num2 = int(input())
operator = input()
result = 0

if operator == "+":
    result = num1 + num2
    if result % 2 == 0:
        print(f"{num1} + {num2} = {result} - even")
    else:
        print(f"{num1} + {num2} = {result} - odd")
if operator == "-":
    result = num1 - num2
    if result % 2 == 0:
        print(f"{num1} - {num2} = {result} - even")
    else:
        print(f"{num1} - {num2} = {result} - odd")
if operator == "*":
    result = num1 * num2
    if result % 2 == 0:
        print(f"{num1} * {num2} = {result} - even")
    else:
        print(f"{num1} * {num2} = {result} - odd")
if operator == "/":
    if num2 == 0:
        print (f"Cannot divide {num1} by zero")
    else:
     result = num1/num2
     print(f"{num1} / {num2} = {result:.2f}")
if operator == "%":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")