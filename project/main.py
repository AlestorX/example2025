from models.artist import artist_menu
from models.event import Event, load_event
from models.customer import customerMenu
from models.ticket import tickets, generateTickets, loadTickets, saveTickets
from models.sale import sales_menu
from models.artist import load_artists

event = load_event()

tickets = loadTickets()

for e in event:
    existing = [t for t in tickets if t.eventId == e.eventId]
    if not existing:
        generateTickets(e)

saveTickets(tickets)

for t in tickets:
    t.showInfo()


def main():

    artists = []
    artists = load_artists()

    while True:
        print("\n=== MAIN MENU ===")
    
        print("1) Artists")
        print("2) Customers")
        print("3) Sales")
        print("4) Ticket")
        print("5) Events")
        print("0) Exit")

        choice = input("Choice: ").strip()

        if choice =="1":
            artist_menu()
        elif choice =="2":
            customerMenu()
        elif choice =="3":
            listTickets()
        elif choice =="4":
            sales_menu()   
        elif choice =="5":
            event1 = Event("Summer Music Festival", "18.05.2026", "18:00", "00:00", artists)
            event1.show_event()
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()

