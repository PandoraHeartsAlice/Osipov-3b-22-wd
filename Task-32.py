class Schoolboy:
    def __init__(self, name, learning_class):
        self.name = name
        self.learning_class = learning_class

    def study(self):
        print(self.name, "I'm studying")


student = Schoolboy("Alex", 8)
student.study()
