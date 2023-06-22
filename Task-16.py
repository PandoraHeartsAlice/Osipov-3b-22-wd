class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def print_info(self):
        print("Named cat", self.name, ",",
              self.age, "age,", "color", self.color)


cat1 = Cat("Pluton", 2, "white")
cat1.print_info()
