from models.artist import artist_menu
from models.event import load_events
from models.customer import customerMenu
from models.ticket import listTickets
from models.sale import sales_menu
from models.artist import load_artists


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
            events = load_events()

            if len(events) == 0:
                print("No events yet.")
            else:
                print("\nEvents:")
                for e in events:
                    print(f"- [{e.eventId}] {e.event_name} ({e.date} {e.start_time}-{e.end_time})")
            
        elif choice == "0":
                print("Bye.")
                break
        
        else:
            print("Invalid  choice.")

if __name__=="__main__":
    main()

