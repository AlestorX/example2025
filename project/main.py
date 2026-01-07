from models.artist import artist_menu
from models.event import Event

def main():
    artists = artist_menu()
    print("\nArtists received in main.py")
    for a in artists:
        a.show()

    event1 = Event ("Summer Music Festival", "18.05.2026", "18:00", "00:00", artists)


    event1.show_event()

if __name__ == "__main__":
    main()
