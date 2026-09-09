class StudentService:

    def __init__(self):
        self.students = []

    def register_student(self, student):
        for existing_student in self.students:
            if existing_student.student_id == student.student_id:
                print("students Exists")
                return
        print(f"{student.name} has been registered.")

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def remove_student_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return
        print("Student not found.")

    def find_student(self, student):
        return student in self.students
    
    def find_student_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.display_information()
                return
        print("Student not found.")

    def find_students_by_course(self, course):
        found = False
        for student in self.students:
            if student.course == course:
                student.display_information()
                found = True
        if not found:
            print("Student not found.")

    def get_student_count(self):
        count = 0
        for student in self.students:
            count += 1
        return count
    
    def display_student(self, student):
        student.display_information()

    def display_all_students(self):
        for student in self.students:
            student.display_information()