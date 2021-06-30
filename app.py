from packages.zoo import Zoo
from packages.animal import Animal



zoo1=Zoo(input("Enter Zoo Name:"))
# zoo1 = Zoo("John's Zoo")
# zoo1.add_lion("Nala").add_lion("Simba").add_tiger("Rajah").add_tiger("Shere Khan").print_all_info()

while True :
    menu=input("1.Add Lion\n2.Add Tiger\n3.Add Bear\n4.Feed\n5.Show All\n6.Quit\nEnter Option:")
    if menu=="1":
        answer1=input("Enter Lion Name:")
        zoo1.add_lion(answer1)
    if menu=="2":
        answer2=input("Enter Tiger Name:")
        zoo1.add_tiger(answer2)
    if menu=="3":
        answer3=input("Enter Bear Name:")
        zoo1.add_bear(answer3)
    if menu=="4":
        zoo1.feed_animals()
    if menu=="5":
        zoo1.print_all_info()
    if menu=="6":
        break
    
    

# zoo1.add_lion("Simba")
# zoo1.add_tiger("Rajah")
# zoo1.add_tiger("Shere Khan")
# zoo1.print_all_info()