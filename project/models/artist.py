from models.person import Person

import os
import csv

class Artist: 
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def show(self):
        print(f"- {self.name} ({self.genre})")


ARTISTS_FILE = "data/artists.csv"

def load_artists():
     # If file doesn't exist, return default artists
     if not os.path.exists(ARTISTS_FILE):
         return [
             Artist("Shakira", "pop"),
             Artist("The weeknd", "R&B"),
             Artist("Rihanna", "pop")
         ]
     
     artists = []
     with open (ARTISTS_FILE, "r", newline="", encoding="utf-8") as f:
         reader = csv.reader(f)
         for row in reader:
             if len(row) != 2:
                 continue
             name = row[0].strip()
             genre = row[1].strip()
             #Skip empty/bad data 
             if name == "" or genre == "":
                  artists.append (Artist(name, genre))

     return artists 



def list_artists(artists):
    if len(artists) == 0:
        print ("No artists yet.")
        return
    
    # Sort by genre first, then name
    artists_sorted = sorted(artists, key=lambda a: (a.genre.strip().lower(), a.name.strip().lower()))

    print("\nArtists (grouped by genre )")
    
    current_genre = None
    for a in artists_sorted:
        genre_clean = a.genre.strip().lower()
        name_clean = a.name.strip()


        # Print a header when genre changes
        if genre_clean !=current_genre:
         current_genre = genre_clean
        print (f"\n{current_genre.upper()}:")
    print (f"- {a.name}")


def artist_menu():
    artists =  load_artists()

    while True:
        print("\n=== Artists Menu ===")
        print("1) List artists")
        print("0) Back")

        choice = input("Choice ").strip()

        if choice == "1":
            list_artists(artists) 
        elif choice == "0":
            print("Back to main menu... ")
            return artists
        else:
            print("Invalid choice.")




