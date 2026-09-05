from .person import Person

class Lecturer(Person):

    def __init__(self, name, address, phone, staff_id, department, salary):
        super().__init__(name, address, phone)

        self.staff_id = staff_id
        self.department = department
        self.__salary = salary

    def teach(self):
        print("I am teaching.")

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary < 0:
            print("Salary must be greater than zero.")
        else:
            self.__salary = salary

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount
        else:
            print("Increase amount must be greater than zero.")

    def display_information(self):
        print(f"Name: {self.name}, Address: {self.address}, Phone: {self.get_phone()}, staff id: {self.staff_id}")

    def perform_role(self):
        print("Teaching Student")
