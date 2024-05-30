import turtle

turtle.shape("turtle")


for i in range (4):
    if i % 2 == 0 :
        
        turtle.forward(200)
        turtle.color("red")
        turtle.right(90)        
    else:
        turtle.forward(200)
        turtle.color("yellow")
        turtle.right(90)
        
 
#Fill fully color in square       
turtle.color("red")

turtle.begin_fill()
for i in range (4):
    if i % 2 == 0 :
        
        turtle.forward(200)
        turtle.right(90)        
    else:
        turtle.forward(200)
        turtle.right(90)
turtle.end_fill()      

turtle.hideturtle()
turtle.done()