city = input()
num = float(input())
commision = 0

if city == "Sofia":
    if 0 <= num <= 500:
        commision = 5/100 * num
        print(f"{commision:.2f}")
    elif 500 <= num <= 1000:
        commision = 7/100 * num
        print(f"{commision:.2f}")
    elif 1000 <= num <= 10000:
        commision = 8/100 * num
        print(f"{commision:.2f}")
    elif num > 10000:
        commision = 12/100 * num
        print(f"{commision:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= num <= 500:
        commision = 4.5/100 * num
        print(f"{commision:.2f}")
    elif 500 <= num <= 1000:
        commision = 7.5/100 * num
        print(f"{commision:.2f}")
    elif 1000 <= num <= 10000:
        commision = 10/100 * num
        print(f"{commision:.2f}")
    elif num > 10000:
        commision = 13/100 * num
        print(f"{commision:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= num <= 500:
        commision = 5.5/100 * num
        print(f"{commision:.2f}")
    elif 500 <= num <= 1000:
        commision = 8/100 * num
        print(f"{commision:.2f}")
    elif 1000 <= num <= 10000:
        commision = 12/100 * num
        print(f"{commision:.2f}")
    elif num > 10000:
        commision = 14.5/100 * num
        print(f"{commision:.2f}")
    else:
        print("error")
else:
    print("error")