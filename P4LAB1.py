#Jalynn Hardin 
#3/26/24
#P4LAB1
#Using loops to draw shapes

import turtle
win = turtle.screen()
timmy = turtle.turtle()

#Add some display options 
timmy.pensize(4)       #increases pensize (takes integer)
timmy.pencolor("blue") #Set pencolor (takes strimg)
timmy.shape("arrow")

#Use a for loop to draw the square
for side in range(4):
    timmy.forward(75)
    timmy.right(90)