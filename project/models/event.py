import os
import csv

from models.artist import Artist, load_artists #we will use artists from artist.py

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
        if len(self.artists) == 0:
                print("- (No artists found)")
        else:
                for a in self.artists:
                    if a is None:
                        continue
                    a.show()

EVENT_FILE = "project/data/events.csv"


def find_artist_by_name(artists, name):
    name_clean = name.strip().lower()
    for a in artists:
        if a.name.strip().lower() == name_clean:
            return a
    return None


def load_events():
    #If file doesn't exists, return some defualt events
    if not os.path.exists(EVENT_FILE):
        default_artists = load_artists()

        beyonce = find_artist_by_name(default_artists, "Beyoncé")
        miles = find_artist_by_name(default_artists, "Miles Davis")


        #Pick some artists for the defualt events
        return [
    Event("E1", "Summer Pop Night", "2026-02-10", "19:00", "22:00", [beyonce] if beyonce is not None else []),
    Event("E2", "Jazz Evening", "2026-02-12", "20:00", "23:00", [miles] if miles is not None else []),
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


            #Skip empty/bad rows

            if eventId == "" or event_name == "" or date == "":
                continue

            event_artists = []
            if artist_names_text != "":
                names = artist_names_text.split ("|")
                for n in names:
                    n = n.strip()
                    if n == "":
                        continue

                    found = find_artist_by_name(artists, n)
                    if found is not None:
                        event_artists.append(found)
                    else:
                       # If artist is not in artists.csv, still show it as an Artist object 
                        event_artists.append(Artist(n, "Unknown"))

            events.append(Event(eventId, event_name, date, start_time, end_time, event_artists))
    return events

