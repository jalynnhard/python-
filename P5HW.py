#Jalynn Hardin
#Date:4/18/24
#P5HW
#Making a math quiz

import random
num1  = random.randint(1, 100)
num2 = random.randint(1, 100)

def add_menu():
    num1  = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f"add {num1} + {num2}")
    correct_answer = num1 + num2
    users_answer = int(input("What is your answer"))
    Number_guesses = 1
    while users_answer != correct_answer:
        Number_guesses += 1
        if users_answer  > correct_answer:
            print("answer is too high")
        if users_answer  < correct_answer:
            print("answer is too low")
        users_answer = int(input("What is your answer"))
    print("ongragulations you got the answer correct")
    print(f"Number of guesses {Number_guesses}")

def subtract_menu():
    num1  = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f"subtract {num1} - {num2}")
    correct_answer = num1 - num2
    users_answer = int(input("What is your answer"))
    Number_guesses = 1
    while users_answer != correct_answer:
        Number_guesses += 1
        if users_answer  > correct_answer:
            print("answer is too high")
        if users_answer  < correct_answer:
            print("answer is too low")
        users_answer = int(input("What is your answer"))
    print("ongragulations you got the answer correct")
    print(f"Number of guesses {Number_guesses}")
    
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
        add_menu()
    if display_menu == "2":
        print("subtract")
        subtract_menu()
    display_menu = input("please choose one of the menu options")   
print("program is ending")

