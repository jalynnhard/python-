#Jalynn Hardin 
#Date:2/22/2024
#P1HW2
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

#Display results
print("\nBudget Summary:")
print(f"Budget: ${budget}")
print(f"Destination: {destination}")
print(f"Gas Expense: ${gas_expense}")
print(f"Accommodation Expense: ${accommodation_expense}")
print(f"Food Expense: ${food_expense}")
print(f"Total Expenses: ${total_expenses}")
print(f"Remaining Budget: ${remaining_budget}")
