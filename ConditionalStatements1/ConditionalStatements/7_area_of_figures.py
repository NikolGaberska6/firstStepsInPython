from math import pi

type = input()

if type == "square":
    lenght = float(input())
    shape_area = lenght * lenght
    print(f"{shape_area:.3f}")
elif type == "rectangle":
    lenght1 = float(input())
    lenght2 = float(input())
    shape_area = lenght1 * lenght2
    print(f"{shape_area:.3f}")

elif type == "circle":
    radius = float(input())
    shape_area = pi * radius * radius
    print(f"{shape_area:.3f}")

elif type == "triangle":
    lenght = float(input())
    height = float(input())
    shape_area = (lenght * height)/2
    print(f"{shape_area:.3f}")