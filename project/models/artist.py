from .person import Person

class Artist(Person):
    def __init__(self, name, genre):
        super().__init__(name)
        self.genre = genre

        def perform(self):
            print(f"{self.name} is performing {self.genre} music!")

            def show_info(self):
                super() .show_info()
                print(f"Genre: {self.genre}")
                