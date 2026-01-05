import csv

FILE_NAME = "artists.csv"


class Artist: 
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def show(self):
        print(f"- {self.name} ({self.genre})")





def add_artist(artists):
    name = input("Artist name: ").strip()
    genre = input("Genre: ").strip()

    if name == "" or genre == "":
        print("Name and genre cannot be empty. ")
        return
    
    for a in artists:
        if a.name.lower() == name.lower():
            print("This artist already exists.")
            return
        
        artists.append(Artist(name, genre))
        print("Artist added!")





def list_artists(artists):
    if len(artists) == 0:
        print ("No artists yet.")
        return
    
    print("Artists:")
    for a in artists:
        a.show()





def artist_menu():
    artists = []
    

    while True:
        print("\n=== Artists Menu ===")
        print("1) Add Artist")
        print("2) List artists")
        print("0) Exit")

        choice = input("Choice ")

        if choice == "1":
            add_artist(artists)
        elif choice == "2":
            list_artists(artists)
        elif choice == "0":
            print("Bye!")
            return artists
        else:
            print("Invalid choice.")





if __name__ == "__main__":
    artist_menu()