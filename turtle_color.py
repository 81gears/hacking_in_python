# https://michael0x2a.com/blog/turtle-examples

import turtle 

painter = turtle.Turtle()

painter.pencolor("blue")
painter.speed(50)

for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("green")
for i in range(50):
    painter.forward(100)
    painter.left(123)
    
turtle.done()
