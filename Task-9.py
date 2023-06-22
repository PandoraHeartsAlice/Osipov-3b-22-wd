class Rectangle:
    def __init__(self, height, width):
        self.width = width
        self.height = height

    def area(self):
        print("area =", self.width*self.height)


rectangle = Rectangle(7, 3)
print(rectangle.area())
