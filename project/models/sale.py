import csv

from models import customer
from models import event
from models import ticket

fileName = "project/data/sales.csv"

class Sale:
    def __init__(self, salesId: int, event: event, customer:customer, ticket: ticket):
        self.salesId = salesId
        self.event = event
        self.customer = customer
        self.ticket = ticket
        self.purchase = False 

    
        
    def save_sale(self):
        try:
            with open(fileName, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    self.salesId,
                    self.event.eventId,
                    self.customer.customerId,
                    self.ticket.ticketId,
                    self.purchase
                ])

        except Exception as e:
            print(f"Erorror can not save sale information:{e}")
 
def make_purchase(Event: event, Customer: customer, Ticket: ticket):
    try:
        if not Ticket.available:
            print("Tickets are sold out for this event.")
            return False
        
        Ticket.available = False # Mark ticket as sold
                
        sale = Sale(
            salesId = 1,
            event = Event,
            customer = Customer,
            ticket = Ticket
        )

        sale.purchase = True

        sale.save_sale()
        print("Purchase successful!")
        return True
        
    except Exception as e:
        print(f"An error occurred during purchase: {e}")
        return False
            
def sales_menu():
    while True:
        print("\n=== SALES MENU ===")
        print("1) Make purchase")
        print("0) Back")

        choice = input("Choice: ").strip()

        if choice == "1":
            print("Purchasing in progress...")
            # which customer is buying?
            customers = customer.loadCustomers()
            if len(customers) == 0:
                print("No customers. Please add customers first.")
                continue
            purchasingcustomer = customers[0] 
            # which artist are they buying from?
            #display a list of artists
            #get the user to pick an artists
            purchasingartist = None 
            # which event are they buying for?
            events = event.load_events()
            if len(events) == 0:
                print("No events. Please add events first.")
                continue

            for ev in events:
                ev.show_event()

            selectedEvent = input("Select event by ID: ").strip()
            # get the usersto pick an event
            #save the selected event into purchasingevent variable
            purchasingevent = None
            for e in events:
                if e.eventId.strip() == selectedEvent:
                    purchasingevent = e
                    break
            if purchasingevent is None:
                print("Invalid event ID.")
                continue

            # which ticket are they buying?
            tickets_list = ticket.loadTickets()
            available_tickets = ticket.getAvailableTickets(purchasingevent.eventId, tickets_list)
            if len(available_tickets) == 0:    
                print("No available tickets for this event.")
                continue

            purchasingticket = available_tickets[0]

            purchasingticket.available = False
            ticket.saveTickets(tickets_list)

            make_purchase(purchasingevent, purchasingcustomer, purchasingticket)
        
        elif choice == "0":
            return
        else:
            print("Invalid choice.")    