#Jalynn Hardin
#Date:4/18/24
#P5HW
#Making a math quiz

print("Welcome to math quiz")



print("MAIN MENU")
print("----------------------------")

num1 = float(input("1 adding random numbers: "))
num2 = float(input("2 Subtracting random numbers: "))

import random 
num1 = random.randint(1, 300)
num2 = random.randint(1, 300)

print("1.The random number is", num1)
print("2.The random number is", num2 )
