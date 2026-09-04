from abc import ABC, abstractmethod
class Person(ABC):

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.__phone = phone


    def eat(self):
        print("I want to eat.")

    def sleep(self):
        print("I want to sleep.")

    def bath(self):
        print("taking my bath")

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        if not phone:
            print("Phone number must not be empty.")
        else:
            self.__phone = phone

    @abstractmethod
    def perform_role(self):
        pass

    def display_information(self):
        print(f"Name: {self.name}, Address: {self.address}, Phone: {self.__phone}")
                  
class Student(Person):

    def __init__(self, name, address, phone, student_id, course, level, score):
        super().__init__(name, address, phone)

        self.student_id = student_id
        self.course = course
        self.level = level
        self.__score = 0
        if 0 <= score <= 100:
            self.set_score(score)
        else:
            print("invalid Score")

    def study(self):
        print("I am Studying")

    def take_exam(self):
        print("I am taking an exam.")

    def register(self):
        print("I have registered my courses.")

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            print("invalid Score")

    def get_score(self):
        return self.__score

    def calculate_grade(self):
        if self.__score >= 70:
            return "A"
        elif self.__score >= 60:
            return "B"
        elif self.__score >= 50:
            return "C"
        elif self.__score >= 40:
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


class UnderGraduatestudent(Student):
    
    def __init__(self, name, address, phone, student_id, course, level, matricNumber, relationship, score):
        super().__init__(name, address, phone, student_id, course, level, score)

        self.__matricNumber = matricNumber
        self.relationship = relationship

    def attend_lectures(self):
            print("attending lectures")

    def take_notes(self):
            print("Taking Notes")

    def display_information(self):
        super().display_information()
        print(f"Matric Number: {self.__matricNumber}")
        print(f"Relationship: {self.relationship}")

    def get_matric_number(self):
        return self.__matricNumber

    def perform_role(self):
        print("Registering")

class Lecturer(Person):

    def __init__(self, name, address, phone, staff_id, department, salary):
        super().__init__(name, address, phone)

        self.staff_id = staff_id
        self.department = department
        self.__salary = salary

    def teach(self):
        print("I am teaching.")

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary < 0:
            print("Salary must be greater than zero.")
        else:
            self.__salary = salary

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount
        else:
            print("Increase amount must be greater than zero.")

    def display_information(self):
        print(f"Name: {self.name}, Address: {self.address}, Phone: {self.get_phone()}, staff id: {self.staff_id}")

    def perform_role(self):
        print("Teaching Student")

class Administrator(Person):
    def __init__(self, name, address, phone, admin_id, department, role):
        super().__init__(name, address, phone)

        self.admin_id = admin_id
        self.department = department
        self.__role = role

    def admit_student(self):
        print("Student admitted.")

    def assigned_matric_number(self):
        print("matric assigned")

    def process_school_fees(self):
        print("processing")

    def get_role(self):
        return self.__role
    def change_role(self, old_role, new_role):
        if self.__role == old_role:
            self.__role = new_role
        else:
            print("Incorrect old role.")


    def display_information(self):
        print(f"Name: {self.name}, Address: {self.address}, Phone: {self.get_phone()}, Admin id: {self.admin_id}")

    def perform_role(self):
        print("Handling Files")


student1 = Student("victor", "kwara", 1001, "STOO1", "computer science", "Monday 9AM", 50)
lecturer1 = Lecturer("Bolu", "kwara", 81111, "tyfu`2", "ICT", 500000)
administrator1 = Administrator("Akorede", "Kwara", 8909, "ihe8989", "IT", "operator")
under_graduate1 = UnderGraduatestudent("Bolu", "Kwara", 7043797036, "456gh", "Computer science", 200, 3345, "single", 20) 
student1.study()
under_graduate1.study()
under_graduate1.sleep()
student1.take_exam()
student1.register()
student1.sleep()
student1.eat()
student1.display_information()
print(administrator1.get_role())

administrator1.change_role("Developer", "Manager")

print(administrator1.get_role())

people = [
    student1,
    lecturer1,
    administrator1,
    under_graduate1
]

for person in people:
    person.display_information()
    print("----------------")


for person in people:
    person.perform_role()
    print("=== ROLES ===")
