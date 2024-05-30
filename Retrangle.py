import turtle

turtle.shape("turtle")
turtle.color("yellow")
for i in range (4):
    if i %2 == 0:
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(100)
        turtle.color("red")
        turtle.left(90)
    
    else: 
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(100)
        turtle.color("blue")
        turtle.left(90)
        
turtle.hideturtle()
turtle.done()