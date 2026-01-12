from models.artist import artist_menu
from models.event import Event
from models.customer import customerMenu
from models.ticket import listTickets
from models.sale import sales_menu
from models.sale import Sale



def main():
    while True:
        print("\n=== MAIN MENU ===")
    
        print("1) Artists")
        print("2) Customers")
        print("3) Ticket")
        print("4) Sales")
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
            Sale()
        elif choice =="5":
            Event.event_menu()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()

