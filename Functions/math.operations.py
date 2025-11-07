def my_function(x, y):
    print(f"Please enter a iteration you want to do (+ - * / %): ")
    iteration = input()
    if iteration == "+":
        return x + y
    elif iteration == "-":
        return abs(x-y)
    elif iteration == "*":
        return x * y
    elif iteration == "/":
        return x/y
    elif iteration == "%":
        return x % y
    else:
        return (f"Please enter a valid operation: {iteration}")

print("Today we will do some math exercises!")
print("Please enter your nums: ")

x = int(input())
y = int(input())

print(my_function(x, y))