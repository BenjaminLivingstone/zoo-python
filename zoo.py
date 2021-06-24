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
    def print_all_info(self):
        print("*"*30, self.name, "*"*30)
        for animal in self.animals:
            animal.display_info()
        print("*"*30, self.name, "*"*30)
        return self
        
class Lion(Zoo):
    def __init__(self, zoo_name):
        super().__init__(zoo_name)  #   Add lions particular 
    def display_info(self):
        print(f"{type(self).__name__}: {self.name}")
class Tiger(Zoo):
    def __init__(self, zoo_name):
        super().__init__(zoo_name)
    def display_info(self):
        print(f"{type(self).__name__}: {self.name}")


zoo1=Zoo(input("Enter Zoo Name:"))
# zoo1 = Zoo("John's Zoo")
# zoo1.add_lion("Nala").add_lion("Simba").add_tiger("Rajah").add_tiger("Shere Khan").print_all_info()

while True :
    menu=input("1.Add Lion\n2.Add Tiger\n3.Show Animals\n4.Quit\nEnter Option:")
    if menu=="1":
        answer1=input("Enter Lion Name:")
        zoo1.add_lion(answer1)
    if menu=="2":
        answer2=input("Enter Tiger Name:")
        zoo1.add_tiger(answer2)
    if menu=="3":
        zoo1.print_all_info()
    if menu=="4":
        break
    

# zoo1.add_lion("Simba")
# zoo1.add_tiger("Rajah")
# zoo1.add_tiger("Shere Khan")
# zoo1.print_all_info()

# ¡Espero que esto parezca un poco repetitivo, y puede usar sus habilidades y conocimientos para reducir parte del código anterior y divertirse haciendo un zoológico en el proceso!

# Esta tarea es deliberadamente abierta. ¡Que te diviertas!

# Debe subir esta tarea con nombre zoo a Github.# BONUS: Debe crear una forma interactiva (while True ;)) oara poder ir creando animales e ir agregándolos al ZOO.