class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def print_info(self):
        print("Name:", self.name)
        print("breed:", self.breed)
        print("Age:", self.age)


dog = Dog("Бобик", "Джек Рассел", 3)
dog.print_info()
