from services.student_service import StudentService

from models import (
    Student,
    UnderGraduateStudent,
    Lecturer,
    Administrator
)


student_service = StudentService()


student1 = Student(
    "victor",
    "kwara",
    "1001",
    "ST001",
    "computer science",
    "100L",
    50
)

student2 = Student(
    "David",
    "Lagos",
    "1002",
    "ST002",
    "computer science",
    "100L",
    80
)

lecturer1 = Lecturer(
    "Bolu",
    "Kwara",
    "81111",
    "STA001",
    "ICT",
    500000
)

administrator1 = Administrator(
    "Akorede",
    "Kwara",
    "8909",
    "ADM001",
    "IT",
    "operator"
)

under_graduate1 = UnderGraduateStudent(
    "Bolu",
    "Kwara",
    "7043797036",
    "ST003",
    "Computer science",
    "200L",
    "3345",
    "single",
    20
)


# Register students
student_service.register_student(student1)
student_service.register_student(student2)
student_service.register_student(under_graduate1)


# Display all students
print("\n=== ALL STUDENTS ===")
student_service.display_all_students()


# Find a student
print("\n=== FIND STUDENT ===")
student = student_service.find_student("ST001")

if student:
    student.display_information()
else:
    print("Student not found.")


# Update score
print("\n=== UPDATE SCORE ===")
student_service.update_student_score("ST001", 85)

student = student_service.find_student("ST001")

if student:
    student.display_information()


# Student count
print("\n=== STUDENT COUNT ===")
print(student_service.get_student_count())


# Average score
print("\n=== AVERAGE SCORE ===")
print(student_service.get_average_score())


# Other OOP demonstration
print("\n=== ROLES ===")

people = [
    student1,
    lecturer1,
    administrator1,
    under_graduate1
]

for person in people:
    person.display_information()
    person.perform_role()
    print("----------------")