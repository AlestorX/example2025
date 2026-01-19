from .artist import Artist



class Event:
    def __init__(self, eventId, event_name, date, start_time, end_time, artists):
        self.eventId = eventId
        self.event_name = event_name
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.artists = artists 

    def show_event(self):
            print("\n=== Event Info ===")
            print("ID:", self.eventId)
            print("Event:", self.event_name)
            print("Date:", self.date)
            print("Time:", self.start_time, "-", self.end_time)

            print("Artists:")
            for a in self.artists:
                a.show()

def event_menu():
    print("\n=== Event Menu ===")
    print("1) Show event info")
    print("0) Back")

    choice = input("Choice: ").strip()

    if choice == "1":
        print("Event logic will run here.")
    elif choice == "0":
        return
    else:
        print("Invalid choice.")