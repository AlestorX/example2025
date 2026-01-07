import csv

class Ticket:
    def __init__(self, ticketId, ticketType, price, available=True)
        self.ticketId = ticketId
        self.ticketType = ticketType
        self.price = price
        self.available = available

    def showInfo(self):
        status = "Available" if self.available else "Sold"
        print(f"ID: {self.ticketId}")
        print(f"Type: {self.ticketType}")
        print(f"Price: {self.price}")
        print(f"Status: {status}")



