try:
    n = int(input("Въведете число: "))
    if n % 3 == 0 and n % 5 == 0:
        print("Divisible")
    else:
        print("Not divisible")
except:
    print("Invalid input")