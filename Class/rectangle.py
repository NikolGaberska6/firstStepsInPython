class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

rect1 = Rectangle(3, 4)
rect2 = Rectangle(9, 3)
rect3 = Rectangle(8, 7)
rect4 = Rectangle(4, 9)

print(f"Area: {rect1.area()}, Perimeter: {rect1.perimeter()}")
print(f"Area: {rect2.area()}, Perimeter: {rect2.perimeter()}")
print(f"Area: {rect3.area()}, Perimeter: {rect3.perimeter()}")
print(f"Area: {rect4.area()}, Perimeter: {rect4.perimeter()}")