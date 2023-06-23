import math


def distance(point):
    x, y = point
    return math.sqrt(x**2 + y**2)


points = [(1, 2), (3, 4), (-1, 5), (6, -3)]
points.sort(key=distance)
print(points)
