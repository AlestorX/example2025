import csv

FILE_NAME = "artists.csv"


class Artist: 
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def show(self):
        print(f"- {self.name} ({self.genre})")





def list_artists(artists):
    if len(artists) == 0:
        print ("No artists yet.")
        return
    
    print("Artists:")
    for a in artists:
        a.show()





def artist_menu():
    artists = [
        Artist("Shakira", "pop"),
        Artist("The Weeknd", "R&B"),
        Artist("Rihanna", "pop")
    ]


    

    while True:
        print("\n=== Artists Menu ===")
        print("1) List artists")
        print("0) Exit")

        choice = input("Choice ").strip()


        if choice == "1":
            list_artists(artists) 
        elif choice == "0":
            print("Bye!")
            return artists
        else:
            print("Invalid choice.")





if __name__ == "__main__":
    artist_menu()
