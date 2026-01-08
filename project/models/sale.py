import csv
from ticket import Ticket
from customer import Customer 
from event import Event

fileName = "sales.csv"

class Sales:
    def __init__(self, salesId, customer, ticket, event_name):
        self.salesId = salesId
        self.customer = customer
        self.ticket = ticket
        self.event_name = event_name

    def makePurchase(self):
        if not self.ticket.available:
            print("Ticket not available.")
            return False
        
        self.ticket.available = False
        self.saveSale()
        print("Purchase successful.")
        return True
    
def saveSale(self):
    with open(fileName, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            self.saleId,
            self.customer.customerId,
            self.customer.name,
            self.event.event_name,
            self.ticket.ticketId,
            self.ticket.ticketType,
            self.ticket.price
        ])
        