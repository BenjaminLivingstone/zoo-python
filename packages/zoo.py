#Cada animal debe tener al menos un nombre, una edad, un nivel de salud y un nivel de felicidad.
from packages.lion import Lion
from packages.tiger import Tiger
from packages.bear import Bear

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name #peso, edad, etc
        self.animals = []        
    def add_lion(self, name):
        self.animals.append(Lion(name))
        return self
    def add_tiger(self, name):
        self.animals.append(Tiger(name))
        return self
    def add_bear(self, name):
        self.animals.append(Bear(name))
        return self    
    def print_all_info(self):
        print("*"*30, self.name, "*"*30)
        for animal in self.animals:
            animal.display_info()
        print("*"*30, self.name, "*"*30)
        return self
    def feed_animals(self):
        for animal in self.animals:
            animal.feed()
        return self      



