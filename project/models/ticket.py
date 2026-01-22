import csv


from .event import Event
from .customer import Customer

ticketFile = "tickets.csv"

class Ticket:
    def __init__(self, ticketId, eventId, ticketType, price, available=True):
        self.ticketId = ticketId
        self.eventId = eventId
        self.ticketType = ticketType
        self.price = price
        self.available = available

    def showInfo(self):
        status = "Available" if self.available else "Sold"
        print(f"ID: {self.ticketId}")
        print(f"Event: {self.eventId}")
        print(f"Type: {self.ticketType}")
        print(f"Price: {self.price}")
        print(f"Status: {status}")

def loadTickets():
    tickets = []
    try:
        with open(ticketFile, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 5:
                    continue
                ticketId, eventId, ticketType, price, available = row
                tickets.append(
                    Ticket(
                        ticketId,
                        eventId,
                        ticketType,
                        float(price),
                        available == "True"
                    )
                )
    except FileNotFoundError:
        print("File not found. Starting with empty data.")
        return []

def saveTickets(tickets):
    with open(ticketFile, "w", newline="") as file:
        writer = csv.writer(file)
        for t in tickets:
            writer.writerow([
                t.ticketId,
                t.eventId,
                t.ticketType,
                t.price,
                t.available
            ])

tickets = loadTickets()

def listTickets():
    if len(tickets) == 0:
        print("No tickets available.")
        return

    for t in tickets:
        t.showInfo()
        print("-" * 20)

