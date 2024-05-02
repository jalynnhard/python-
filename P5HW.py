#Jalynn Hardin
#Date:4/18/24
#P5HW
#Making a math quiz

import random
num1  = random.randint(1, 100)
num2 = random.randint(1, 100)



print("Welcome to math quiz")

print("MAIN MENU")
print("----------------------------")

print("1.Adding Random Numbers")
print("2.Subtract Random Numbers")
print("3.Exit")
display_menu = input("please choose one of the menu options")

while display_menu != "3":    
    if display_menu == "1":
        print("add")
       # add_menu()
    if display_menu == "2":
        print("subtract")
        #subtract_menu()
    display_menu = input("please choose one of the menu options")   
print("program is ending")