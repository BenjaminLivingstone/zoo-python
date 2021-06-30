# from packages.zoo import Zoo

class Animal:
    def __init__(self, name, age=10, health=20, happiness=20):
        self.name=name
        self.age=age
        self.health=health
        self.happiness=happiness

    def feed(self):
        self.health+=10
        self.happiness+=10
        return self
