class Worker:
    def __init__(self, name, age, cash):
        self.name = name
        self.age = age
        self.cash = cash

    def Show(self):
        print("Worker named", self.name, ",", self.age,
              "years old, and salary of", self.cash, "dollars.")


worker1 = Worker("Alex", 18, 500)
worker1.Show()
