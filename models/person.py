from abc import ABC, abstractmethod
class Person(ABC):

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.__phone = phone


    def eat(self):
        print("I want to eat.")

    def sleep(self):
        print("I want to sleep.")

    def bath(self):
        print("taking my bath")

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        if not phone:
            print("Phone number must not be empty.")
        else:
            self.__phone = phone

    @abstractmethod
    def perform_role(self):
        pass

    def display_information(self):
        print(f"Name: {self.name}, Address: {self.address}, Phone: {self.__phone}")
         