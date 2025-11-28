import math
try:
    number = int(input("Въведете цяло число: "))
    result = math.sqrt(number)
    print(result)
except:
    print("Invalid number")
finally:
    print("Good Bye")
