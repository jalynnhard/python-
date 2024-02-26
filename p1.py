# Step 3: Ask user to enter their budget
budget = float(input("Enter your budget: $"))

# Step 4: Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Step 5: Ask user for the amount they will spend on gas
gas_expense = float(input("Enter the amount you will spend on gas: $"))

# Step 6: Ask user for the amount they will spend on accommodation
accommodation_expense = float(input("Enter the amount you will spend on accommodation: $"))

# Step 7: Ask user for the amount they will spend on food
food_expense = float(input("Enter the amount you will spend on food: $"))

# Step 8: Add expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Step 9: Subtract expenses from budget
remaining_budget = budget - total_expenses

# Step 10: Display results
print("\nBudget Summary:")
print(f"Budget: ${budget}")
print(f"Destination: {destination}")
print(f"Gas Expense: ${gas_expense}")
print(f"Accommodation Expense: ${accommodation_expense}")
print(f"Food Expense: ${food_expense}")
print(f"Total Expenses: ${total_expenses}")
print(f"Remaining Budget: ${remaining_budget}")

