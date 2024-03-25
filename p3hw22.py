#Hors worked at job
def calculate_overtime_pay(hours_worked, pay_rate):
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        overtime_hours = 0
        overtime_pay = 0
    return overtime_hours, overtime_pay

#Pay for hours
def calculate_regular_pay(hours_worked, pay_rate):
    if hours_worked > 40:
        regular_pay = 40 * pay_rate
    else:
        regular_pay = hours_worked * pay_rate
    return regular_pay 

# Function to display gross pay
def display_gross_pay(employee_name, pay_rate, hours_worked, overtime_hours, overtime_pay, regular_pay):
    gross_pay = overtime_pay + regular_pay
    print("Employee Name:", employee_name)
    print("Pay Rate:", pay_rate)
    print("Number of Hours Worked:", hours_worked)
    print("Overtime Hours:", overtime_hours)
    print("Overtime Pay:", overtime_pay)
    print("Pay for Regular Hours:", regular_pay)
    print("Gross Pay:", gross_pay)
    print("----------------------------------------------")
# Main function
def main():
    # Get input from user
    employee_name = input("Enter name of employee: ")
    hours_worked = float(input("Enter number of hours the employee worked this week: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    # Calculate overtime pay and regular pay
    overtime_hours, overtime_pay = calculate_overtime_pay(hours_worked, pay_rate)
    regular_pay = calculate_regular_pay(hours_worked, pay_rate)

    # Display gross pay
    display_gross_pay(employee_name, pay_rate, hours_worked, overtime_hours, overtime_pay, regular_pay)

# Call the main function
if __name__ == "__main__":
    main()
