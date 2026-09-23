from .person import Person
from utils.validators import validate_score
from utils.validators import has_passed


class Student(Person):

    def __init__(self, name, address, phone, student_id, course, level, score):
        super().__init__(name, address, phone)

        self.student_id = student_id
        self.course = course
        self.level = level
        self.__score = 0
        self.set_score(score)

    def study(self):
        print("I am Studying")

    def take_exam(self):
        print("I am taking an exam.")

    def register(self):
        print("I have registered my courses.")

    def set_score(self, score):
        if validate_score(score):
            self.__score = score
        else:
            print("Invalid score")

    def get_score(self):
        return self.__score

    def calculate_grade(self):
        if self.__score >= 70:
            return "A"
        elif self.__score >= 60:
            return "B"
        elif self.__score >= 50:
            return "C"
        elif has_passed(self.__score):
            return "D"
        elif self.__score >= 0:
            return "F"
        else:
            return "Failed"

    def display_information(self):
        print(
            f"Name: {self.name}, Address: {self.address}, Phone: {self.get_phone()}, "
            f"Student ID: {self.student_id}, Course: {self.course}, Level: {self.level}, "
            f"Score: {self.get_score()}, Grade: {self.calculate_grade()}"
        )

    def perform_role(self):
        print("Attend Class")