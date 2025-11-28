try:
    length = int(input("Въведете дължината на правоъгълника: "))
    weight = int(input("Въведете ширината на правоъгълника: "))
    area = length * weight
    print(f"The area is: {area}")
except:
    print("Invalid input")