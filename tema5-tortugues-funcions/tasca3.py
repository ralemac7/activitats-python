import turtle

tortuga = turtle.Turtle()

tortuga.pensize(5)
tortuga.speed(4)
tortuga.pu()
tortuga.goto(-100, 0)
tortuga.pd()

def poligon(costats, color, tamany):
    angle = ( 360 / costats)
    tortuga.color(color)
    for i in range(costats):
        tortuga.fd(tamany)
        tortuga.lt(angle)

poligon(3, "#FF0000", 50)
tortuga.penup()
tortuga.fd(100)
tortuga.pendown()
poligon(5, "#00FF00", 90)
tortuga.penup()
tortuga.fd(150)
tortuga.pendown()
poligon(6, "#0000FF", 20)

turtle.done()