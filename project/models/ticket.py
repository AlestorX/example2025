import csv

fileName = "tickets.csv"

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

def loadTickets():
    tickets = []
    try:
        with open(fileName, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                ticketId, ticketType, price, available = row
                tickets.append(
                    Ticket(
                        ticketId,
                        ticketType,
                        float(price),
                        available == "True"
                    )
                )
    except FileNotFoundError:
        pass
    return tickets

def saveTickets(tickets):
    with open(fileName, "w", newline="") as file:
        writer = csv.writer(file)
        for t in tickets:
            writer.writerow([
                t.ticketId,
                t.ticketType,
                t.price,
                t.available
            ])
