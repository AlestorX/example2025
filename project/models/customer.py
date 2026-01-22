import csv
from models.person import Person


customerFile = "customers.csv"
saveFile = "sales.csv"


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
        with open(customerFile, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4:
                    continue
                customerId, name, age, email = row
                customers.append(Customer(name, int(age), email, customerId))
    except FileNotFoundError:
        print("File not found. Starting with empty data.")
        return []


def saveCustomer(customer):
    with open(customerFile, "a", newline="") as file:
        write = csv.writer(file)
        write.writerow([
            customer.customerId,
            customer.name,
            customer.age,
            customer.email
        ])


def addCustomer(customers):
    try:
        name = input("Name: ").strip()
        age = int(input("Age: ").strip())
        email = input("Email: ").strip()

        if age < 0:
            print("Invlid Age.")
            return
        
        customerId = f"c{len(customers) + 1}"

        customer = Customer(name, age, email, customerId)
        customers.append(customer)
        saveCustomer(customer)

        print("Customer has been added.")

    except ValueError:
        print("Age must be a number.")


def listCustomer(customers):
    if len(customers) == 0:
        print("No customers yet.")
        return
    
    print("\nCustomers:")
    for c in customers:
        c.showInfo()
        print("-" * 20)


def showCustomerPurchases(customerId):
    print(f"\nPurchases for customer {customerId}:")
    found = False

    try:
        with open(saveFile, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                salesId, eventId, cId, ticketId, purchase = row
                if cId == customerId and purchase == "True":
                    print(f"Event: {eventId} | Ticket: {ticketId}")
    except FileNotFoundError:
        print("File not found. Starting with empty data.")
        return []
    if not found:
        print("No purchases found.")


def customerMenu():
    customers = loadCustomers()
    
    while True:
        print("\n=== Customer Menu ===")
        print("1. Add New Customer")
        print("2. List Customers")
        print("3. Show Customer Purchases")
        print("0. Exit")

        choice = input("Choice (write down number): ").strip()

        if choice == "1":
            addCustomer(customers)
        elif choice == "2":
            listCustomer(customers)
        elif choice == "3":
            cId = input("Enter Customer ID: ").stipr()
            showCustomerPurchases(cId)
        elif choice == "0":
            print("Bye!")
            return customers
        else:
            print("Invalid Choice.")



