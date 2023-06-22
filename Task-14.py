class Student:
    def __init__(self, name, surname, age, speciality):
        self.name = name
        self.surname = surname
        self.age = age
        self.speciality = speciality

    def print_info(self):
        print(self.name, "-", self.surname, ",",
              self.age, "age,", self.speciality)


person = Student("Alex", "Burbukil", 18, "dev")
person.print_info()
