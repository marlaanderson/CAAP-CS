# Marla Anderson
# Lab 4
# 8/5/2018

# Imports the turtle graphics module
import turtle
 
# creates a turtle (pen) an sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")

# setting out box sizes to the n sq pixels per box
boxSize = 10
 

# myPen.setheading(n) points pen to given angle direction.
# where n queals the angle.
# 0 points to the right, 90 to go up, 180 to go to the left 270 to go down

# Positions myPen in top left area of the screen
# This should change according to the image size you want to make and the size of your boxes ("pixels")
# This canvas is currently set to 200*200 pixels or a 20x20 box of 10 sq pixels each
myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0) 

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)       

# Here is an example of how to draw a box using the box function      
# Comment this out when you draw your own images
box(boxSize)
 

# Challenge functions (2 bonus pts each) 
# You need to make shapes with each
#def circle(intRadius):
#def triangle(intLength): #This can be an equilateral triangle
#def save_image(): # saves the screen to an image/vector file

# These are the instructions on how to move "myPen" around after drawing a box.
# penup() lifts the pen so it doesn't draw anything and can be moved freely
# pendown() puts the oen down and it draws as it moves
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()
 
# You will save your drawings as lists.
# This first list stores the color values
pallet_1 = ["#FFFFFF" , "#FFFF00" , "#000000" , "#61380B" , "#F4FA58"]
# Your drawings are stored using a "list of lists" where each value within every list
# element is the index of the color in the pallet list
# Banana
pixels_1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,2,2,3,3,2,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,2,4,1,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,2,4,4,1,2,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,2,4,4,1,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,4,4,1,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,1,1,2,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,4,1,2,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,2,4,1,1,2,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,2,4,1,3,2,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

# Mario
pallet_2 = ["#4B610B" , "#FAFAFA" , "#DF0101" , "#FE9A2E"]
pixels_2 = [[1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1]]
pixels_2.append([1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_2.append([1,1,1,0,0,0,3,3,3,3,3,0,3,1,1,1])
pixels_2.append([1,1,0,3,0,3,3,3,3,3,3,0,3,3,3,1])
pixels_2.append([1,1,0,3,0,0,3,3,3,3,3,3,0,3,3,3])
pixels_2.append([1,1,0,0,3,3,3,3,3,3,3,0,0,0,0,1])
pixels_2.append([1,1,1,1,3,3,3,3,3,3,3,3,3,3,1,1])
pixels_2.append([1,1,1,0,0,2,0,0,0,0,2,0,1,1,1,1])
pixels_2.append([1,1,0,0,0,2,0,0,0,0,2,0,0,0,1,1])
pixels_2.append([0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0])
pixels_2.append([3,3,3,0,2,3,2,2,2,2,3,2,0,3,3,3])
pixels_2.append([3,3,3,3,2,2,2,2,2,2,2,2,3,3,3,3])
pixels_2.append([3,3,3,2,2,2,2,1,1,2,2,2,2,3,3,3])
pixels_2.append([1,1,1,2,2,2,1,1,1,1,2,2,2,1,1,1])
pixels_2.append([1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1])
pixels_2.append([0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0])

# Add your own drawings here
# Pacman
pallet_3 =["#FFFFFF" , "#FD0101" , "#021FFA"]
pixels_3 = [[0,0,0,0,0,1,1,1,1,1,1,0,0,0]]
pixels_3.append([0,0,0,1,1,1,1,1,1,1,1,1,0,0])
pixels_3.append([0,0,1,1,0,0,1,1,1,1,0,0,1,0])
pixels_3.append([0,1,1,0,0,0,0,1,1,0,0,0,0,0])
pixels_3.append([0,1,1,0,0,2,2,1,1,0,0,2,2,0])
pixels_3.append([1,1,1,0,0,2,2,1,1,0,0,2,2,1])
pixels_3.append([1,1,1,1,0,0,1,1,1,1,0,0,1,1])
pixels_3.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_3.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_3.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_3.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_3.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_3.append([1,1,0,1,1,1,0,0,1,1,1,0,1,1])
pixels_3.append([1,0,0,0,1,1,0,0,1,1,0,0,0,1])

#Alien
pallet_4 = ["#FFFFFF" , "#A711F3" , "#CCCBCD"]
pixels_4 = [[0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0]]
pixels_4.append([0,0,0,0,2,1,1,0,0,0,0,0,0,0,0,0,2,1,1,0,0,0,0])
pixels_4.append([0,0,0,0,0,1,1,2,0,0,0,0,0,0,2,2,0,1,1,0,0,0,0])
pixels_4.append([0,0,0,0,0,0,2,1,1,0,0,0,0,0,2,1,1,0,0,0,0,0,0])
pixels_4.append([0,0,0,0,2,2,2,1,1,2,2,2,2,2,2,1,1,2,0,0,0,0,0])
pixels_4.append([0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0])
pixels_4.append([0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0])
pixels_4.append([0,0,2,1,1,1,1,0,2,1,1,1,1,1,1,0,2,1,1,1,1,0,0])
pixels_4.append([2,2,2,1,1,1,1,2,2,1,1,1,1,1,1,2,2,1,1,1,1,2,0])
pixels_4.append([2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_4.append([2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_4.append([2,1,1,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,2,1,1])
pixels_4.append([2,1,1,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,2,1,1])
pixels_4.append([2,1,1,0,2,1,1,0,0,0,0,0,0,0,0,0,2,1,1,0,2,1,1])
pixels_4.append([0,1,1,0,0,1,1,2,2,2,0,0,2,2,2,2,0,1,1,0,0,1,1])
pixels_4.append([0,0,0,0,0,0,2,1,1,1,1,0,2,1,1,1,1,0,0,0,0,0,0])
pixels_4.append([0,0,0,0,0,0,0,2,2,2,2,0,0,2,2,2,2,0,0,0,0,0,0])

#Mushroom
pallet_5 = ["#FFFFFF" , "#000000" , "#FD0101"]
pixels_5 = [[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0]]
pixels_5.append([0,0,0,1,1,2,2,2,2,0,0,1,1,0,0,0])
pixels_5.append([0,0,1,0,0,2,2,2,2,0,0,0,0,1,0,0])
pixels_5.append([0,1,0,0,2,2,2,2,2,2,0,0,0,0,1,0])
pixels_5.append([0,1,0,2,2,0,0,0,0,2,2,0,0,0,1,0])
pixels_5.append([1,2,2,2,0,0,0,0,0,0,2,2,2,2,2,1])
pixels_5.append([1,2,2,2,0,0,0,0,0,0,2,2,0,0,2,1])
pixels_5.append([1,0,2,2,0,0,0,0,0,0,2,0,0,0,0,1])
pixels_5.append([1,0,0,2,2,0,0,0,0,2,2,0,0,0,0,1])
pixels_5.append([1,0,0,2,2,2,2,2,2,2,2,2,0,0,2,1])
pixels_5.append([1,0,2,2,1,1,1,1,1,1,1,1,2,2,2,1])
pixels_5.append([0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,0])
pixels_5.append([0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0])
pixels_5.append([0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0])
pixels_5.append([0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0])
pixels_5.append([0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0])

#Smiley
pallet_6 = ["#FFFFFF" ,"#000000" , "#F8D441" , "#8C4402" , "#E8287E"]
pixels_6 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_6.append([0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,1,1,1,0,0,0,0,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2,2,1,1,0,0,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0])
pixels_6.append([0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0])
pixels_6.append([0,0,0,1,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,1,0,0,0])
pixels_6.append([0,0,0,1,2,2,1,1,1,1,0,1,2,2,2,2,2,2,1,1,1,1,0,0,1,2,2,1,0,0,0])
pixels_6.append([0,0,1,2,2,1,1,1,1,1,0,0,1,2,2,2,2,1,1,1,1,1,0,0,0,1,2,2,1,0,0])
pixels_6.append([0,0,1,2,2,1,1,1,1,1,0,0,1,2,2,2,2,1,1,1,1,1,0,0,0,1,2,2,1,0,0])
pixels_6.append([0,1,2,2,2,1,1,1,1,0,0,0,1,2,2,2,2,1,1,1,1,0,0,0,0,1,2,2,2,1,0])
pixels_6.append([0,1,2,2,1,0,0,0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0,0,0,1,2,2,1,0])
pixels_6.append([0,1,2,2,1,0,0,0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0,0,0,1,2,2,1,0])
pixels_6.append([1,2,2,2,1,0,0,0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0,0,0,1,2,2,2,1])
pixels_6.append([1,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1])
pixels_6.append([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_6.append([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_6.append([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_6.append([0,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,0])
pixels_6.append([0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,1,0])
pixels_6.append([0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,1,0])
pixels_6.append([0,0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,1,0,0])
pixels_6.append([0,0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,3,3,3,3,1,2,2,1,0,0])
pixels_6.append([0,0,0,1,2,2,1,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,3,3,1,2,2,1,0,0,0])
pixels_6.append([0,0,0,1,2,2,2,1,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,1,2,2,2,1,0,0,0])
pixels_6.append([0,0,0,0,1,2,2,2,1,1,3,3,3,3,4,4,4,4,4,4,4,1,1,2,2,2,1,0,0,0,0])
pixels_6.append([0,0,0,0,0,1,1,2,2,2,1,1,1,3,4,4,4,4,1,1,1,2,2,2,1,1,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,0,1,1,2,2,2,2,1,1,1,1,1,2,2,2,2,1,1,0,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,2,2,1,1,1,0,0,0,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0])

#Unicorn
pallet_7 = ["#FFFFFF" , "#000000" , "#F781BE" , "#FF0000" , "#FF8000" , "#FACC2E" , "#FFFF00" , "#BFFF00" , "#04B431" , "#0B6121" , "#04B4AE" , "#0101DF" , "#A901DB" , "#D358F7" , "#D8D8D8" , "#58FAF4"]
pixels_7 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_7.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0,0,1,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,0,0,0,0,3,3,3,3,3,0,0,0,0,1,1,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,0,0,1,14,1,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,0,0,0,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,0,1,14,14,1,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,5,5,5,0,0,4,4,4,4,4,4,4,4,4,1,1,1,3,3,1,14,14,1,0,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,5,5,5,5,5,5,5,4,4,4,4,4,1,1,0,1,3,1,14,14,14,1,0,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,7,7,0,0,0,6,0,6,6,6,5,5,5,5,5,5,5,5,4,4,4,1,0,0,1,1,14,14,14,1,0,0,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,7,7,0,0,0,0,0,0,0,6,6,6,6,6,6,5,5,5,5,5,4,1,0,0,0,1,14,14,14,14,1,2,2,2,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,7,7,7,7,7,7,7,7,0,6,6,6,6,6,6,6,5,5,5,5,4,1,0,0,0,1,14,14,14,1,2,2,2,2,2,2,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,5,5,1,1,1,1,0,0,0,0,1,1,1,1,2,2,2,2,2,2,2,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,0,0,7,7,7,7,7,7,7,7,6,6,6,6,6,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,0,0,2,2,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,7,7,7,7,7,6,6,6,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,2,0])
pixels_7.append([0,0,0,0,0,0,0,8,8,8,8,8,8,8,7,7,7,7,7,7,7,6,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0])
pixels_7.append([0,0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0])
pixels_7.append([0,0,0,0,8,8,0,0,0,0,8,8,8,8,8,8,8,8,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0])
pixels_7.append([0,0,0,0,8,0,0,0,0,0,0,8,8,8,8,8,8,8,8,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,9,9,9,9,9,8,8,8,8,8,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,9,9,9,9,9,9,9,9,9,9,8,8,8,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0])
pixels_7.append([0,0,0,9,9,9,9,9,9,9,9,9,9,9,9,9,9,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0])
pixels_7.append([0,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
pixels_7.append([9,9,9,0,0,9,9,9,9,9,9,9,9,9,9,9,9,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
pixels_7.append([9,0,0,0,0,0,0,9,9,9,9,9,9,9,9,9,9,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,10,10,10,10,10,10,10,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0])
pixels_7.append([0,0,0,0,0,0,0,10,10,10,10,10,10,10,10,10,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,8,6,1,0,0,0,0,1,0,0,])
pixels_7.append([10,10,0,0,0,10,10,10,10,10,10,10,10,10,10,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,8,6,6,1,0,0,0,1,0,0])
pixels_7.append([0,10,10,10,10,10,10,10,10,10,10,10,10,10,10,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,8,0,6,4,1,1,1,0,0,0])
pixels_7.append([0,0,0,10,10,10,10,10,10,10,10,10,10,10,10,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,15,8,6,6,4,2,0,0,0,0])
pixels_7.append([0,0,0,0,0,11,11,11,11,11,11,11,11,11,11,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,15,8,8,6,4,4,0,0,0,0])
pixels_7.append([11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,12,0,8,8,6,0,4,4,2,0,0])
pixels_7.append([0,11,11,11,11,11,11,11,11,11,11,11,11,11,11,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,12,15,15,8,8,6,6,4,2,2,0])
pixels_7.append([0,0,0,11,11,11,11,11,11,11,11,11,11,11,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,12,15,15,8,8,6,6,4,4,0,2])
pixels_7.append([0,0,0,0,0,0,11,11,11,11,11,11,11,11,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,12,12,15,0,8,8,6,6,4,4,2])
pixels_7.append([0,0,0,12,12,12,12,12,12,12,12,12,12,12,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,12,15,15,8,8,6,6,4,4,2])
pixels_7.append([0,12,12,12,12,12,12,12,12,12,12,12,12,12,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,12,12,15,15,8,8,6,6,6,4,4])
pixels_7.append([12,12,12,12,12,12,12,12,12,12,12,12,12,12,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,12,12,12,15,15,8,0,6,6,4,0])
pixels_7.append([0,0,0,0,12,12,12,12,12,12,12,12,12,12,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,12,12,12,15,15,8,8,6,6,6,4])
pixels_7.append([0,0,0,13,13,13,13,13,13,13,13,13,13,13,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,12,12,0,15,15,8,8,8,6,6,4])
pixels_7.append([0,0,13,13,13,13,13,13,13,13,13,13,13,13,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,12,12,12,15,15,15,8,8,0,6,6])
pixels_7.append([0,13,13,13,13,13,13,13,13,13,13,13,13,13,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,12,12,15,15,0,8,8,8,6,0])

#Groot
pallet_8 = ["#FFFFFF" , "#000000" , "#B45F04" , "#8A4B08" , "#0B610B"]
pixels_8 = [[0,0,0,0,0,0,0,0,0,0,4,0,1,0,0,0,0,0,0]]
pixels_8.append([0,0,4,0,0,4,1,0,1,0,0,1,1,0,1,0,0,0,0])
pixels_8.append([0,0,0,1,0,1,1,4,2,1,1,4,1,1,1,4,0,0,0])
pixels_8.append([0,1,4,1,1,2,1,1,2,1,2,1,1,1,4,1,0,0,0])
pixels_8.append([0,0,1,2,1,2,1,2,1,2,1,1,1,2,1,1,0,0,0])
pixels_8.append([0,0,1,3,2,1,2,2,3,2,1,2,3,3,2,1,0,0,0])
pixels_8.append([0,0,1,2,2,2,3,2,2,2,2,3,2,2,2,1,0,0,0])
pixels_8.append([0,0,0,1,2,3,2,2,2,2,3,2,2,2,1,0,0,0,0])
pixels_8.append([0,0,0,1,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0])
pixels_8.append([0,0,0,1,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0])
pixels_8.append([0,0,0,1,2,0,1,2,2,2,2,1,0,2,1,0,0,0,0])
pixels_8.append([0,0,0,1,2,1,1,2,2,2,2,1,1,2,1,0,0,0,0])
pixels_8.append([0,0,0,1,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0])
pixels_8.append([0,0,0,1,2,1,2,2,2,2,2,2,1,2,1,0,4,0,0])
pixels_8.append([0,0,0,1,2,2,1,1,1,1,1,1,2,2,1,0,1,0,4])
pixels_8.append([0,0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,1,1,0])
pixels_8.append([0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,2,1,1])
pixels_8.append([0,0,4,0,0,0,0,1,2,2,1,0,0,0,1,2,1,4,0])
pixels_8.append([4,0,1,0,0,0,1,1,3,2,1,1,1,1,2,1,0,0,0])
pixels_8.append([0,1,1,0,4,1,2,1,1,3,2,1,2,2,1,0,0,0,0])
pixels_8.append([1,1,2,1,1,2,1,0,1,2,3,1,1,1,0,0,0,0,0])
pixels_8.append([0,0,1,2,2,1,0,0,1,2,2,1,0,0,0,0,0,0,0])
pixels_8.append([0,0,0,1,1,4,0,1,2,2,1,0,0,0,0,0,0,0,0])
pixels_8.append([0,0,0,0,0,0,0,1,2,3,1,0,0,0,0,0,0,0,0])
pixels_8.append([0,0,0,0,0,0,1,2,3,3,2,1,0,0,0,0,0,0,0])
pixels_8.append([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0])
pixels_8.append([0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0])
pixels_8.append([0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0])
pixels_8.append([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0])
pixels_8.append([0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0])
pixels_8.append([0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0])
pixels_8.append([0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0])
pixels_8.append([0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0])
pixels_8.append([0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0])
pixels_8.append([0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0])





# This function takes a pallet and pixel list (matrix) to draw the picture
# You are to write this function
def draw(pallet,pixels):
    for i in pixels:
        for j in i:
            myPen.color(pallet[j])
            box(boxSize)
            myPen.forward(boxSize)
            myPen.penup()
        myPen.setheading(180)
        myPen.forward(len(i)*boxSize)
        myPen.setheading(270)
        myPen.forward(boxSize)
        myPen.setheading(0)



# Should give the user a list of the possible drawing pieces you have and ask which one to draw
def main():
    choice = int(input("Choose a picture: \n1.Banana \n2.Mario \n3.Pacman \n4.Alien \n5.Mushroom \n6.Smiley \n7.Unicorn \n8.Baby Groot \n>"))
    if choice ==1:
        draw(pallet_1, pixels_1)
    elif choice ==2:
        draw(pallet_2, pixels_2)
    elif choice ==3:
        draw(pallet_3, pixels_3)
    elif choice ==4:
        draw(pallet_4, pixels_4)
    elif choice ==5:
        draw(pallet_5, pixels_5)
    elif choice ==6:
        draw(pallet_6, pixels_6)
    elif choice ==7:
        draw(pallet_7, pixels_7)
    elif choice ==8:
        draw(pallet_8, pixels_8)
    else:
        print("Incorrect input. Please enter an integer 1-6: ")
	# You need this to prevent the window from closing after drawing
    turtle.done()

main()


#Tests
def test1():
    for i in pixels_1:
        for j in i:
            myPen.color(pallet_1[j])
            box(boxSize)
            myPen.forward(boxSize)
            myPen.penup()
        myPen.setheading(180)
        myPen.forward(len(i)*boxSize)
        myPen.setheading(270)
        myPen.forward(boxSize)
        myPen.setheading(0)

def test2():
    for i in pixels_2:
        for j in i:
            myPen.color(pallet_2[j])
            box(boxSize)
            myPen.forward(boxSize)
            myPen.penup()
        myPen.setheading(180)
        myPen.forward(len(i)*boxSize)
        myPen.setheading(270)
        myPen.forward(boxSize)
        myPen.setheading(0)

def test3():
    for i in pixels_3:
        for j in i:
            myPen.color(pallet_3[j])
            box(boxSize)
            myPen.forward(boxSize)
            myPen.penup()
        myPen.setheading(180)
        myPen.forward(len(i)*boxSize)
        myPen.setheading(270)
        myPen.forward(boxSize)
        myPen.setheading(0)

def test4():
    for i in pixels_4:
        for j in i:
            myPen.color(pallet_4[j])
            box(boxSize)
            myPen.forward(boxSize)
            myPen.penup()
        myPen.setheading(180)
        myPen.forward(len(i)*boxSize)
        myPen.setheading(270)
        myPen.forward(boxSize)
        myPen.setheading(0)

def test5():
    for i in pixels_5:
        for j in i:
            myPen.color(pallet_5[j])
            box(boxSize)
            myPen.forward(boxSize)
            myPen.penup()
        myPen.setheading(180)
        myPen.forward(len(i)*boxSize)
        myPen.setheading(270)
        myPen.forward(boxSize)
        myPen.setheading(0)

def test6():
    for i in pixels_6:
        for j in i:
            myPen.color(pallet_6[j])
            box(boxSize)
            myPen.forward(boxSize)
            myPen.penup()
        myPen.setheading(180)
        myPen.forward(len(i)*boxSize)
        myPen.setheading(270)
        myPen.forward(boxSize)
        myPen.setheading(0)

def test7():
    for i in pixels_7:
        for j in i:
            myPen.color(pallet_7[j])
            box(boxSize)
            myPen.forward(boxSize)
            myPen.penup()
        myPen.setheading(180)
        myPen.forward(len(i)*boxSize)
        myPen.setheading(270)
        myPen.forward(boxSize)
        myPen.setheading(0)

def test8():
    for i in pixels_8:
        for j in i:
            myPen.color(pallet_8[j])
            box(boxSize)
            myPen.forward(boxSize)
            myPen.penup()
        myPen.setheading(180)
        myPen.forward(len(i)*boxSize)
        myPen.setheading(270)
        myPen.forward(boxSize)
        myPen.setheading(0)