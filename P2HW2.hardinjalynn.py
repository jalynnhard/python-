#Jalynn Hardin
#3/5/24
#P2HW2
#Grading assignment for test

#First make the list 
#second we input the values
#Third we got to the results
#fourth we find the lowest grade
#fith we find the highest grade 
#six we find the sum of the grades 
#seventh we find the average of the grades

#List name 
nums = []

nums.append(61)
nums.append(88)
nums.append(78.5)
nums.append(92)
nums.append(65.5)
nums.append(90 )

print(nums)

#Enter grades from different test
num1 = float(input("Enter grade for module 1: "))
num2 = float(input("Enter grade for module 2: "))
num3 = float(input("Enter grade for module 3: "))
num4 = float(input("Enter grade for module 4: "))
num5 = float(input("Enter grade for module 5: "))
num6 = float(input("Enter grade for module 6: "))

#Results of the list 
print("------------Results------------")

#Lowest grade
list_low = min(nums)
print(f"Lowest grade: {list_low}")

#Highest grade
list_max = max(nums)
print(f"Highest grade: {list_max}")

#Sum of grade
list_sum = sum(nums)
print(f"Sum of grades: {list_sum}")

#Get the average 
average = sum(nums) / len(nums)
print("average:", average)



