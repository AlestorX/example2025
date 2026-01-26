import os
import csv


BASE_DIR = os.path.dirname(os.path.dirname(__file__)) 
ticketFile = os.path.join(BASE_DIR, "data", "tickets.csv")



class Ticket:
    def __init__(self, ticketId, eventId, ticketType, price, quantity):
        self.ticketId = ticketId
        self.eventId = eventId
        self.ticketType = ticketType
        self.price = float(price)
        self.quantity = int(quantity)
        
    @property
    def available(self):        
        return self.quantity > 0


    def showInfo(self):
        """Display Ticket details"""
        status = "Available" if self.available else "Sold"
        print(f"Quantity: {self.quantity}")
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
                ticketId, eventId, ticketType, price, quantity = row
                quantity = int(quantity)
                tickets.append(
                    Ticket(
                        ticketId,
                        eventId,
                        ticketType,
                        float(price),
                        quantity
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

# Generate tickets for an event and save them
def generateTickets(event):
    global tickets
    if 'tickets' not in globals():
        tickets = loadTickets()
    

    ticketType = [
        {"type": "VIP", "price": 100.0, "quantity": 5},
        {"type": "General", "price": 50.0, "quantity": 10 },
    ]

    #Find the next ticket ID
    nextId = len(tickets) + 1

    for t in ticketType:
        for _ in range(t["quantity"]):
            ticketId = f"T{nextId}"
            tickets.append(Ticket(ticketId, event.eventId, t["type"], t["price"], True))
            nextId += 1
    
    # Save all tickets to CSV
    saveTickets(tickets)
    print(f"Tickets generated for event {event.event_name}.")
    
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
            if t.quantity > 0:
                available += t.quantity
            else:
                sold += 1
        print(f"Event {eventId}: Sold = {sold} | Available = {available}")

# Global tickets variable
tickets = loadTickets()
def saveTickets(tickets_list):
    with open(ticketFile, "w", newline="") as file:
        writer = csv.writer(file)
        for t in tickets_list:
            writer.writerow([t.ticketId, t.eventId, t.ticketType, t.price, t.quantity])
RESTOCK_QTY = 5

def restockAllIfSoldOut(tickets_list):
    # if every ticket quantity is 0 = restock all back to 5
    if tickets_list and all(t.quantity <= 0 for t in tickets_list):
        for t in tickets_list:
            t.quantity = RESTOCK_QTY
        saveTickets(tickets_list)


