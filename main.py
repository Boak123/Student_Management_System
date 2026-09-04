
from models.person import Person
from models.student import Student
from models.undergraduate import UnderGraduatestudent
from models.lecturer import Lecturer
from models.administrator import Administrator


student1 = Student("victor", "kwara", 1001, "STOO1", "computer science", "Monday 9AM", 50)
lecturer1 = Lecturer("Bolu", "kwara", 81111, "tyfu`2", "ICT", 500000)
administrator1 = Administrator("Akorede", "Kwara", 8909, "ihe8989", "IT", "operator")
under_graduate1 = UnderGraduatestudent("Bolu", "Kwara", 7043797036, "456gh", "Computer science", 200, 3345, "single", 20) 
student1.study()
under_graduate1.study()
under_graduate1.sleep()
student1.take_exam()
student1.register()
student1.sleep()
student1.eat()
student1.display_information()
print(administrator1.get_role())

administrator1.change_role("Developer", "Manager")

print(administrator1.get_role())

people = [
    student1,
    lecturer1,
    administrator1,
    under_graduate1
]

for person in people:
    person.display_information()
    print("----------------")


for person in people:
    person.perform_role()
    print("=== ROLES ===")
