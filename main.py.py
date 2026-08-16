class Person:

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def eat(self):
        print("I want to eat.")

    def sleep(self):
        print("I want to sleep.")

    def bath(self):
        print("taking my bath")

    def display_information(self):
            print(f"Name: {self.name}, Address: {self.address}, Phone: {self.phone}")
                  
class Student(Person):

    def __init__(self, name, address, phone, student_id, course, level):
        super().__init__(name, address, phone)

        self.student_id = student_id
        self.course = course
        self.level = level

    def study(self):
        print("I am Studying")

    def take_exam(self):
        print("I am taking an exam.")

    def register(self):
        print("I have registered my courses.")

    def display_information(self):
        print(f"Name: {self.name}, Address: {self}, Phone: {self.phone}, Student id: {self.student_id}")


class UnderGraduateGstudent(Student):
    
    def __init__(self, name, address, phone, student_id, course, level, matricNumber, relationship,):
        super().__init__(name, address, phone, student_id, course, level)

        self.matricNumber = matricNumber
        self.relationship = relationship

    def attend_lectures(self):
            print("attending lectures")

    def take_notes(self):
            print("Taking Notes")

    def display_information(self):
        print(f"Name: {self.name}, Address: {self}, Phone: {self.phone}, Student id: {self.student_id}")


class Lecturer(Person):

    def __init__(self, name, address, phone, staff_id, department, salary):
        super().__init__(name, address, phone)

        self.staffID = staff_id
        self.department = department
        self.salary = salary

    def teach(self):
        print("I am teaching.")

    def display_information(self):
        print(f"Name: {self.name}, Address: {self}, Phone: {self.phone}, staff id: {self.staff_id}")

class Administrator(Person):
    def __init__(self, name, address, phone, admin_id, department, role):
        super().__init__(name, address, phone)

        self.admin_id = admin_id
        self.department = department
        self.role = role

    def admit_student(self):
        print("Student admitted.")

    def assigned_matric_number(self):
        print("matric assigned")

    def process_school_fees(self):
        print("processing")

    def display_information(self):
        print(f"Name: {self.name}, Address: {self}, Phone: {self.phone}, Admin id: {self.admin_id}")


student1 = Student("victor", "kwara", 1001, "STOO1", "computer science", "Monday 9AM")
lecturer1 = Lecturer("Bolu", "kwara", 81111, "tyfu`2", "ICT", 500000)
administrator1 = Administrator("Akorede", "Kwara", 8909, "ihe8989", "IT", "operator")
under_graduate1 = UnderGraduateGstudent("Bolu", "Kwara", 889, "Math", 300, 205, "Tola", "single") 
student1.study()
under_graduate1.study()
under_graduate1.sleep()
student1.take_exam()
student1.register()
student1.sleep()
student1.eat()
student1.display_information()
