class Student:
    def __init__(self, name, surname, course, grades):
        self.name = name
        self.surname = surname
        self.course = course
        self.grades = grades

    def calculate_average_grade(self):
        total = sum(self.grades)
        average = total / len(self.grades)
        return average


student = Student("Иван", "Иванов", 3, [5, 5, 5, 4, 5])
average_grade = student.calculate_average_grade()
print("Средний балл студента", student.name, student.surname, average_grade)
