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