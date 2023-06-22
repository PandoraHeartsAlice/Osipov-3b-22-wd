class Book:
    def __init__(self, name, author, age, genre):
        self.name = name
        self.author = author
        self.age = age
        self.genre = genre

    def say_my_name(self):
        print(f'{self.name}, {self.author} ({self.age}), {self.genre}')


book1 = Book("Маленький принц", "Антуан де Сент-Экзюпери",
             1942, "философская сказка.")
book1.say_my_name()
