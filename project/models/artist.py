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
     if not os.path.excits(ARTISTS_FILE):
         return [
             Artist("Shakira", "pop"),
             Artist("the weeknd", "R&B"),
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
             artists.append (Artist(name, genre))

     return artists 



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




