import csv
from models.person import Person

fileName = "customers.csv"
class Customer(Person):
    def __init__(self, name, age, email, customerId):
        super().__init__(name)
        self.age = age
        self.email = email
        self.customerId = customerId

    def showInfo(self):
        print(f"ID: {self.customerId}") 
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        