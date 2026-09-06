from .person import Person

class Administrator(Person):
    def __init__(self, name, address, phone, admin_id, department, role):
        super().__init__(name, address, phone)

        self.admin_id = admin_id
        self.department = department
        self.__role = role

    def admit_student(self):
        print("Student admitted.")

    def assigned_matric_number(self):
        print("matric assigned")

    def process_school_fees(self):
        print("processing")

    def get_role(self):
        return self.__role
    def change_role(self, old_role, new_role):
        if self.__role == old_role:
            self.__role = new_role
        else:
            print("Incorrect old role.")


    def display_information(self):
        print(f"Name: {self.name}, Address: {self.address}, Phone: {self.get_phone()}, Admin id: {self.admin_id}")

    def perform_role(self):
        print("Handling Files")