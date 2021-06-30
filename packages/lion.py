from packages.animal import Animal

class Lion(Animal):
    def __init__(self, name, age=10, health=20, happiness=20):
        super().__init__(name,age,happiness,health)  #   Add lions particular 
    def display_info(self):
        print(f"{type(self).__name__}: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}")  
    def feed(self):
        self.health+=10
        self.happiness+=10
        return self
