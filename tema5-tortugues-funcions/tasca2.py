import turtle

tortuga = turtle.Turtle()

def triangle():
    for i in range(3):
        tortuga.fd(100)
        tortuga.lt(120)
def pentagon():
    for i in range(5):
        tortuga.fd(100)
        tortuga.lt(72)
def hexagon():
    for i in range(6):
        tortuga.fd(100)
        tortuga.lt(60)

tortuga.pensize(5)
tortuga.speed(4)
tortuga.color("#FE5000")

tortuga.pu()
tortuga.goto(-250, 0)
tortuga.pd()

triangle()
tortuga.pu()
tortuga.fd(150)
tortuga.pd()
pentagon()
tortuga.pu()
tortuga.fd(200)
tortuga.pd()
hexagon()

turtle.done()