class Person:

    def eat(self):
        print("I want to eat.")

    def sleep(self):
        print("I want to sleep.")

class Student(Person):

    def study(self):
        print("I am Studying")

    def take_exam(self):
        print("I am taking an exam.")

    def register(self):
        print("I have registered my courses.")

        def under_graduate_student(self):

            def attend_lectures(self):
                print("attending lectures")

            def take_notes(self):
                print("Taking Notes")

class Lecturer(Person):

    def teach(self):
        print("I am teaching.")

class Administrator(Person):

    def admit_student(self):
        print("Student admitted.")

student1 = Student()
student1.study()
student1.take_exam()
student1.register()
student1.sleep()
student1.eat()