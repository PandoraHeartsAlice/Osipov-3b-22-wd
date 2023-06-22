class Car:
    def __init__(self, mark, model, age, cost):
        self.mark = mark
        self.model = model
        self.age = age
        self.cost = cost

    def print_info(self):
        print(self.mark, "-", self.model,
              ",", self.age, ",", self.cost)


car1 = Car("BMW", "123321", 2023, 30000000)
car1.print_info()
