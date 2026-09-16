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
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None


    def remove_undergraduate(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return

        print("Student not found.")

    def find_students_by_course(self, course):
        students_by_course = []

        for student in self.students:
            if student.course == course:
                students_by_course.append(student)

        return students_by_course

    def find_by_level(self, level):
        students_by_level = []

        for student in self.students:
            if student.level == level:
                students_by_level.append(student)

        return students_by_level

    def get_matric_number(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student.get_matric_number()

        return None

    def get_undergraduate_count(self):
        return len(self.students)

    def display_all_undergraduates(self):
        for student in self.students:
            student.display_information()