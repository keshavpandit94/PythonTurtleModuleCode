import turtle

side = 8
lenght = 90

# side = int(input("The number of sides the polygon should have is : "))

# lenght = int(input("The lenght of each side the polygon should have is : "))

turtle.shape("turtle")
turtle.color("green")

turtle.begin_fill()

for i in range(side):
    if i % 2 == 0 :
        turtle.forward(lenght)
        turtle.color("red")
        turtle.right(360/side)
    else:
       turtle.forward(lenght)
       turtle.color("green")
       turtle.right(360/side)

turtle.end_fill()

turtle.hideturtle()
turtle.done()