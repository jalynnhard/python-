#jALYNN hARDIN
#dATE:2/27/24
#p2lab1 = math expressions and f-strings

mpg = float(input("Enter the cars mpg: "))
cost_gas = float(input("how much is a galoinr of gas: "))

#Calculate cost of driving 20 miles
miles_20 = (20/mpg) * cost_gas

#Calculate cost of driving 75 miles
miles_75 = (75/mpg) * cost_gas

#Calculate cost of driving 500 miles
miles_500 = (500/mpg) * cost_gas

#output info to user 
print(f"cost to drive 20 miles is ${miles_20:.2f}")
print(f"cost to drive 75 miles is ${miles_75:.2f}")
print(f"cost to drive 500 miles is ${miles_500:.2f}")


