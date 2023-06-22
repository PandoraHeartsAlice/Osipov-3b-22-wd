class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


person = Person("Alex", 18)
person.print_info()
