#jalynn hardin
#Date:2/29/24
#P2HW1
#This program calculates and displays travel expenses

#What is the users budget
budget = float(input("Enter your budget: $"))

# What is the users travel destination
destination = input("Enter your travel destination: ")

#how much will you spend on gas
gas_expense = float(input("Enter the amount you will spend on gas: $"))

#how much will you spend on accomindations
accommodation_expense = float(input("Enter the amount you will spend on accommodation: $"))

#how much will you spend on food
food_expense = float(input("Enter the amount you will spend on food: $"))

#Add all expenses
total_expenses = gas_expense + accommodation_expense + food_expense

#Subtract expenses from budget
remaining_budget = budget - total_expenses

print("-----------Travel expenses-------------")
print("Location: Ashville")
print("Intitial budget: $1200.0")
print("Fuel: $250.0")
print("Accomadation: $300.0")
print("Food: $200.0")
print("----------------------------------------")

print("Remaining balance: $450.0")
