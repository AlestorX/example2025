import os
import csv

from .artist import Artist, load_artists #we will use artists from artist.py



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
            if len(self.artists) ==0:
                print("- (No artists found)")
            else:
                for a in self.artists:
                    a.show()

EVENT_FILE = "data/events.csv"


def load_event():
    #If file doesn't exists, return some defualt events
    if not os.path.exists(EVENT_FILE):
        defualt_artists = load_artists

        #Pick some artists for the defualt events
        return [
            Event("E1", "Summer Pop Night", "2026-02-10", "19:00", "22:00", [find_artist_by_name(default_artists, "Beyoncé")]),
            Event("E2", "Jazz Evening", "2026-02-12", "20:00", "23:00", [find_artist_by_name(default_artists, "Miles Davis")]),
        ]

    events = []
    artists = load_artists()  # list of Artist objects (from artists.csv)

    with open(EVENT_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            # eventId,event_name,date,start_time,end_time,artist_names
            if len(row) != 6:
                continue


            eventId = row[0].strip()
            event_name = row[1].strip()
            date = row[2].strip()
            start_time = row[3].strip()
            end_time = row[4].strip()
            artist_names_text = row[5].strip()






