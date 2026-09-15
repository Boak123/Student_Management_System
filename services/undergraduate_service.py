class UndergraduateService:

    def __init__(self):
        self.students = []

    def register_undergraduate(self, student):
        for existing_student in self.students:
            if existing_student.student_id == student.student_id:
                print("Undergraduate student already exists.")
                return

        self.students.append(student)
        print(f"{student.name} has been registered as an undergraduate student.")

    def find_undergraduate(self, student_id):
        found = False
        for student in self.students:
            if student.student_id == student_id:
                student.display_information()
                found = True

        if not found:
            print("Student not found.")


    def remove_undergraduate(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return

        print("Student not found.")

    def find_students_by_course(self, course):
        self.students_by_course = []

        for student_course in self.students:
            if student_course.course == course:
                self.students_by_course.append(student_course)
        
        if not self.students_by_course:
            print("Student not found.")
        return self.students_by_course
