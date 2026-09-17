from services.student_service import StudentService
from services.undergraduate_service import UndergraduateService
from utils.validators import validate_score


from models import (
    Student,
    UnderGraduateStudent,
    Lecturer,
    Administrator
)


student_service = StudentService()
undergraduate_service = UndergraduateService()


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
undergraduate_service.register_undergraduate(under_graduate1)


# Display all students
print("\n=== ALL STUDENTS ===")
student_service.display_all_students()

print("\n=== UNDERGRADUATE STUDENTS ===")
undergraduate_service.display_all_undergraduates()


# Find a student
print("\n=== FIND STUDENT ===")
student = student_service.find_student("ST001")

if student:
    student.display_information()
else:
    print("Student not found.")


print("\n=== FIND UNDERGRADUATE ===")

undergraduate = undergraduate_service.find_undergraduate("ST003")

if undergraduate:
    undergraduate.display_information()
else:
    print("Student not found.")


# Update score
print("\n=== UPDATE SCORE ===")
student_service.update_student_score("ST001", 85)

student = student_service.find_student("ST001")

if student:
    student.display_information()

print("\n=== FIND BY COURSE ===")

students = undergraduate_service.find_students_by_course("Computer science")

for student in students:
    student.display_information()


print("\n=== FIND BY LEVEL ===")

students = undergraduate_service.find_by_level("200L")

for student in students:
    student.display_information()


print("\n=== MATRIC NUMBER ===")

matric_number = undergraduate_service.get_matric_number("ST003")

if matric_number:
    print(f"Matric Number: {matric_number}")
else:
    print("Student not found.")


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