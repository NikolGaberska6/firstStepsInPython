
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is a {self.color} shape")


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)           #we can replace super() with Shape
        self.radius = radius

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)           #we can replace super() with Shape
        self.width = width

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)            #we can replace super() with Shape
        self.width = width
        self.height = height

circle = Circle("red", True, 5)
circle.describe()
print(circle.color)
#print(circle.filled)
#print(circle.radius)
square = Square("blue", False, 6)
square.describe()
print(square.color)
#print(square.filled)
#print(square.width)
triangle = Triangle("yellow", True, 2, 6)
triangle.describe()
print(triangle.color)
#print(triangle.filled)
#print(triangle.width)
#print(triangle.height)


