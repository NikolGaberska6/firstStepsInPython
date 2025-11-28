try:
    year = int(input("Въведете годината, която искате да проверите: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Годината е вискосна")
    else:
        print("Годината не е високосна")
except:
    print("Invalid input")