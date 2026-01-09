import csv

from project.models.ticket import Ticket
from project.models.customer import Customer
from project.models.event import Event


FILENAME = "sales.csv"   # constant


class Sales:
    def __init__(self, salesId, customer, ticket, event):
        self.salesId = salesId              # int
        self.customer = customer            # Customer object
        self.ticket = ticket                # Ticket object
        self.event = event                  # Event object
        self.purchase = False               # Purchase status (boolean)

    def makePurchase(self):
        """
        Handles the ticket purchase process
        """
        if not self.ticket.available:
            print("Ticket not available.")
            return False

        self.ticket.available = False
        self.purchase = True
        self.saveSale()

        print("Purchase successful.")
        return True

    def saveSale(self):
        """
        Saves sale information to CSV file
        """
        try:
            with open(FILENAME, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    self.salesId,
                    self.customer.customerId,
                    self.customer.name,
                    self.event.event_name,
                    self.ticket.ticketId,
                    self.ticket.ticketType,
                    self.ticket.price
                ])
        except Exception as e:
            print("Error saving sale:", e)
