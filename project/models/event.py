from artist import Artist



class Event:
    def __int__(self, event_name, date, start_time, end_time, artists):
        self.event_name = event_name
        self.date = date
        self.start_time = start_time

        self.artists = artists 

        def show_event(self):
            print("\n=== Event Info ===")
            print("Event:", self.event_name)
            print("Date:", self.date)
            print("Time:", self.start_time, "-", self.end_time)

            