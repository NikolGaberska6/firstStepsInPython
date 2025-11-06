def calculate_square_area(a):
    area = a * a
    return area

def calculate_square_perimeter(a):
    perimeter = 4 * a
    return perimeter

def calculate_rectangle_area(a, b):
    area = a * b
    return area

def calculate_rectangle_perimeter(a, b):
    perimeter = 2 * a + 2 * b
    return perimeter

def print_rectangle_info():
    height = int(input("Enter the height"))
    width = int(input("Enter the width"))
    area = calculate_rectangle_area(height, width)
    perimeter = calculate_rectangle_perimeter(height, width)
    print(f"Rectangle({height} x {width})\n-area:{area}\n-perimeter:{perimeter}")

print_rectangle_info()



