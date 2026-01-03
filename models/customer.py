from person import Person 

class Customer(Person):
    def __init__(self, name, age, email):
        super().__init__(name)
        self.age = age
        self.email = email