import csv

FILE_NAME = "artists.csv"


class Artist: 
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def show(self):
        print(f"- {self.name} ({self.genre})")


def add_artist(artists):
    name = input("Artist name")
    genre = input("Genre: ")

    if name == "" or genre == "":
        print("Name and genre cannot be empty. ")
        return
    
    for a in artists:
        if a.name.lower() == name.lower():
            print("this artist already exists.")
            return
        
        artists.append(Artist(name, genre))
        print("Artist added!")