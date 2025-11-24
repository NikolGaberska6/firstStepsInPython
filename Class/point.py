import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)


point1 = Point(1, 2)
point2 = Point(3,4)
point3 = Point(5, 8)

print(Point.distance(point1, point2))
print(Point.distance(point2, point3))
print(Point.distance(point1, point3))
