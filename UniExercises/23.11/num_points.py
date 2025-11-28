points = int(input("Въведете броя на точките си: "))
if points < 45:
    print("A1")
elif 45 <= points < 60:
    print("A2")
elif 60 <= points < 75:
    print("B1")
elif 75 <= points < 90:
    print("B2")
else:
    print("C1")