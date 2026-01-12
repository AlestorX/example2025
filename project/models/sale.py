import csv


from models.customer import Customer
from models.event import Event

fileName = "sales.csv"

class Sale:
    def __init__(self, salesId, event, customer, ticket):
        self.salesId = salesId
        self.event = event
        self.customer = customer
        self.ticket = ticket
        self.purchase = False 

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
 

def sales_menu():
    while True:
        print("\n=== SALES MENU ===")
        print("1) Make purchase")
        print("0) Back")

        choice = input("Choice: ").strip()

        if choice == "1":
            print("Purchasing in progress...")
        elif choice == "0":
            return
        else:
            print("Invalid choice.")