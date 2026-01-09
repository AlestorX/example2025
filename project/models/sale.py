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

    