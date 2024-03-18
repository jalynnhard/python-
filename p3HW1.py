#jalynn Harin
#3/17/2024
#P3HW1
#Finding results for final grade

#List name 
nums = []

nums.append(86.5)
nums.append(80)
nums.append(76.9)
nums.append(90)
nums.append(79)
nums.append(88 )

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


print("--------------------------------")

print("Your grade is: B")