import csv

from models.ticket import Ticket
from models.customer import Customer
from models.event import Event

fileName = "sales.csv"

class Sale:
    def __init__(self, event, customer, ticket):
        self.event = event
        self.customer = customer
        self.ticket = ticket
        self.purchase = False #Purchase status

    def make_purchase(self):
        try:
            if not self.ticket.available:
                print("Tickets are sold out for this event.")
                return False
            
            # change ticket status 
            self.ticket.available = False
            self.purchase = True

            self.save_sale()
            print("Purchase successful!")
            return True
        
        except Exception as e:
            print(f"An error occurred during purchase: {e}")
            return False