import csv
from ticket import Ticket
from customer import Customer 

fileName = "sales.csv"

class Sales:
    def __init__(self, event, customer, ticket):
        self.event= event
        self.customer = customer
        self.ticket = ticket

    def makePurchase(self):
        if not self.ticket.available:
            print("Ticket not available.")
            return False
        
        self.ticket.available = False
        self.saveToFile()

        print("Purchase successful.")
        return True
    
def saveToFile(self):
    with open(fileName, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            self.event.event_name,
            self.customer.customerID,
            self.ticket.ticketType,
            self.ticket.price
        ])