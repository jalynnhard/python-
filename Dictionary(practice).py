#Dictionary - each item has a key and value

cars = {"tesla":"model s", "toyota":"prius", "chevy":"corola"}

#Get item from dictionary
print(cars["toyota"])

#see all keys in dictionary
print(list(cars.keys()))

print(list(cars.values()))

#Add to dictionary
cars["ford"] = "f-150"

#Print the dictionary 
print(cars)

#Edit item in list
cars["toyota"] = "sequoia"
print(cars)

#Remove item from dictionary
del (cars)["tesla"]
print(cars)

friends = {"besties":["jan", "frank", "melissa",], "aqq":["dan", "sam"]}

#get value using the key
print(friends["besties"][1])