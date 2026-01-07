import csv

fileName = "sales.csv"

class Sales:
    def __init__(self, event, customer, ticket):
        self.evet = event
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
    