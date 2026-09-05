from .student import Student

class UnderGraduateStudent(Student):
    
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
