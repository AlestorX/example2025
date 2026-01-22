import csv


ticketFile = "tickets.csv"


class Ticket:
    def __init__(self, ticketId, eventId, ticketType, price, available=True):
        self.ticketId = ticketId
        self.eventId = eventId
        self.ticketType = ticketType
        self.price = float(price)
        self.available = available

    def showInfo(self):
        """Display Ticket details"""
        status = "Available" if self.available else "Sold"
        print(f"ID: {self.ticketId}")
        print(f"Event ID: {self.eventId}")
        print(f"Type: {self.ticketType}")
        print(f"Price: £{self.price:.2f}")
        print(f"Status: {status}")

# Load tickets from CSV
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
        print("Ticket file not found. Starting with empty data.")
    return tickets

# Save all tickets back to file
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

# List tickets with categorization
def listTickets():
    if not tickets:
        print("No tickets available.")
        return
    
    #Group tickets by event
    ticketByEvent = {}
    for t in tickets:
        ticketByEvent.setdefault(t.eventId, []).append(t)

    # Display tickets grouped by event
    for eventId in sorted(ticketByEvent.keys()):
        print(f"\n=== Tickets for Event ID: {eventId} ===")
        for t in sorted(ticketByEvent[eventId], key=lambda x: x.ticketType.low()):
            t.showInfo()
        print("-" * 30)

# Check available tickets for a specific evet
def getAvailableTickets(eventId, tickets):
    """Return a list of available tickets for a given event"""
    available = [t for t in tickets if t.eventId == eventId and t.available]
    return available 

# Report to show data
def ticketReport(tickets):
    ticketByEvent = {}
    for t in tickets:
        ticketByEvent.setdefaul(t.eventId, []).append(t)

    print("\n=== Ticket Sales Report ===")
    for eventId, ticketList in ticketByEvent.items():
        sold = 0
        available = 0
        for t in ticketList:
            if t.available:
                available += 1
            else:
                sold += 1
        print(f"Event {eventId}: Sold = {sold} | Available = {available}")

# Global tickets variable
tickets = loadTickets()

