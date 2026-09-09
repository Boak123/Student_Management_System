class StudentService:

    def __init__(self):
        self.students = []

    def register_student(self, student):
        for existing_student in self.students:
            if existing_student.student_id == student.student_id:
                print("Student already exists.")
                return

        self.students.append(student)
        print(f"{student.name} has been registered.")

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return

        print("Student not found.")

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    def find_students_by_course(self, course):
        found = False

        for student in self.students:
            if student.course == course:
                student.display_information()
                found = True

        if not found:
            print("Student not found.")

    def update_student_score(self, student_id, score):
        student = self.find_student(student_id)

        if student:
            student.set_score(score)
            return

        print("Student not found.")

    def get_average_score(self):
        if not self.students:
            raise ValueError(
                "Cannot calculate average score for an empty list of students."
            )

        total_score = sum(
            student.get_score() for student in self.students
        )

        return total_score / len(self.students)

    def get_student_count(self):
        return len(self.students)

    def display_student(self, student):
        student.display_information()

    def display_all_students(self):
        for student in self.students:
            student.display_information()