year = int(input("Въведете годината: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Годината е високосна!")
else:
    print("Годината не е високосна!")