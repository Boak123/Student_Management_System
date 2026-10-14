from utils.validators import validate_student_data
from config.settings import MAX_STUDENTS
from exceptions.student_exceptions import StudentNotFoundError
from models.student import Student

class StudentService:

    def __init__(self):
        self.students = []

    def register_student(self, student: Student) -> None:

        if not validate_student_data(
            student.name,
            student.get_phone(),
            student.student_id,
            student.get_score()
        ):
             print("Invalid student data.")
             return

        for existing_student in self.students:
            if existing_student.student_id == student.student_id:
                print("Student already exists.")
                return
        if len(self.students) >= MAX_STUDENTS:
            print("Maximum capacity full")
            return
        
        self.students.append(student)
        print(f"{student.name} has been registered.")

    def remove_student(self, student_id: str) -> None:
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return

        print("Student not found.")

    def find_students_by_course(self, course: str) -> list[Student]:
        students_by_course = []

        for student in self.students:
            if student.course == course:
                students_by_course.append(student)

        return students_by_course

    def find_student_by_id(self, student_id: str) -> Student:
        for student in self.students:
            if student.student_id == student_id:
                return student

        raise StudentNotFoundError(f"Student with ID {student_id} not found.")


    def update_student_score(self, student_id: str, score: float) -> None:
        try:
            student = self.find_student_by_id(student_id)
            student.set_score(score)
            print(f"Score updated for {student.name}.")
        except StudentNotFoundError:
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

    def get_student_count(self) -> int:
        return len(self.students)

    def display_student(self, student):
        student.display_information()

    def display_all_students(self) -> None:
        for student in self.students:
            student.display_information()