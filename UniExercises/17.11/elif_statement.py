points = float(input("Въведете своите точки: "))

if points >= 90:
    print("Отличен 6")
elif 80 <= points < 90:
    print("Мн. Добър 5")
elif 70 <= points < 80:
    print("Добър 4")
elif 60 <= points < 70:
    print("Среден 3")
else:
    print("Слаб 2")