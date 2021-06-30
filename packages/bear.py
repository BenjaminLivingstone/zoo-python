from packages.animal import Animal

class Bear(Animal):
    def __init__(self, name, age=10, health=20, happiness=20):
        super().__init__(name,age,happiness,health)
    def display_info(self):
        print(f"{type(self).__name__}: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}") 
    def feed(self):
        self.health+=5
        self.happiness+=5
        return self
