class StudentService:
    def register_student(self, student):
        print(f"{student.name} has been registered.")

    def display_student(self, student):
        student.display_information()