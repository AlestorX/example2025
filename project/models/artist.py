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

    