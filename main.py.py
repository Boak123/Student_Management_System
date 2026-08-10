class Person:

    def __init__(self, name, address, ID):
        self.name = name
        self.address = address
        self.ID = ID

    def eat(self):
        print("I want to eat.")

    def sleep(self):
        print("I want to sleep.")

    def bath(bath):
        print("taking my bath")

class Student(Person):

    def __init__(self, studentID, course, timetable):
        self.studentID = studentID
        self.course = course
        self.timetable = timetable

    def study(self):
        print("I am Studying")

    def take_exam(self):
        print("I am taking an exam.")

    def register(self):
        print("I have registered my courses.")

class under_graduate_student(Student):
    def __init__(self, matricNumber, relationship):
        self.matricNumber = matricNumber
        self.relationship = relationship

        def attend_lectures(self):
            print("attending lectures")

        def take_notes(self):
            print("Taking Notes")

class Lecturer(Person):

    def __init__(self, staffID, course_teaching):
        self.staffID = staffID
        self.course_teaching = course_teaching

    def teach(self):
        print("I am teaching.")

class Administrator(Person):
    def __init__(self, emergencydata, id):
        self.emergencydata = emergencydata
        self.id = id

    def admit_student(self):
        print("Student admitted.")

    def assigned_matric_number(self):
        print("matric assigned")

    def process_school_fees(self):
        print("processing")

student1 = Student()
student1.study()
student1.take_exam()
student1.register()
student1.sleep()
student1.eat()