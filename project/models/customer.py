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

def loadCustomers():
    customers = []
    try:
        with open(fileName, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                customerId, name, age, email = row
                customers.append(
                    Customer(name, int(age), email, customerId)
                )
    except FileNotFoundError:
        pass
    return customers

def saveCustomer(customer):
    with open(fileName, "a", newline="") as file:
        write = csv.writer(file)
        write.writerow([
            customer.customerId,
            customer.name,
            customer.age,
            customer.email
        ])