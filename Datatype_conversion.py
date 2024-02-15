'''
#Converting datatype 

weekly_rate = input("Enter your weekly pay: ")

weekly_pay = float(weekly_rate)

print("your weekly pay is",weekly_rate)

#See what the datatype is for a variable 
print(type(weekly_rate))

#Display bi-weekly pay
print("Every two weeks you make", "$" + str(weekly_rate * 2), "dollars")

print("Every two weeks you make", weekly_rate * 2, "dollars")

'''

#In your homework do not hardcode. Get a vaules from user. Remember to convert to a number datatype

num1 = 3
num2 = 5

print(num1, "*", num2, "=", num1 * num2)


#Using exponents

print(num1**num2)

(num1, "raised to the power of", num2, "is", num1**num2)
