#List
nums = []

#Add values to the list - "hard code"
nums.append(3)
nums.append(5.785)
nums.append(63.0)

print(nums)

num1 = float(input("Enter a float value: "))

#Add variable to list
nums.append(num1)

nums.append(float(input("Enter a float value: ")))


#gET THE SUM OF ALL VALUES IN THE LIST
list_sum = sum(nums)
print(f"The sum of the list is : {list_sum}")

print(sum([1,1,1,1,1,1,1,]))

#Get the minimum value from the list
list_min = min(nums)
print(list_min)
print(f"The mallest value of the list is : {list_min}")

#Get maximum value from the list
list_max = max(nums)
print(f"The largest value of the list is : {list_max}")

#Get the length of the list
list_length = len(nums)
print(f"The list has {list_length} items")

