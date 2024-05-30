from turtle import *

speed('fastest')  # Using 'fastest' for quicker drawing

# Making the turtle face upwards
right(-90)

# Using an acute angle between the base and the Y's branch
angle = 30

# Method for plotting a Y
def y(length, lvl):
    if lvl > 0:
        # Normalizing the color value for green
        green_value = 254 // lvl / 255
        pencolor(0, green_value, 0)
        
        # Drawing the base
        forward(length)
        
        right(angle)
        
        # Calling recursion for the right subtree
        y(0.8 * length, lvl-1)
        
        pencolor(0, green_value, 0)
        
        left(2 * angle)
        
        # Calling recursion for the left subtree
        y(0.8 * length, lvl-1)
        
        pencolor(0, green_value, 0)
        
        right(angle)
        forward(-length)

# Drawing the tree of length 40 and level 8
y(40, 8)

hideturtle()
done()
