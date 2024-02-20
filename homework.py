#
#
#

#Street is a string datatype
street = input("what is your street")

#Convert to in() in the same line 
house_num = input("what is your house number? ")

#house_num = input("what is your house number? "))

house_num = input("what is your house number? ")

#convert to int() separately
house_num = int(house_num)

Neigh_num = house_num + 2

#print our address & neighbor address
print("your address is",house_num,street)
print("your neighbor's address is",neigh_num,street)
