import turtle

def cargol():
    for i in range(20):
        turtle.pencolor("#964B00")
        turtle.pensize(5)
        turtle.forward(i + 3)
        turtle.right(45)

    turtle.pensize(7)
    turtle.pencolor("#83F28F")
    turtle.forward(45)
    turtle.right(90)
    turtle.forward(20)

    turtle.right(30)
    turtle.forward(10)
    
    turtle.backward(10)
    turtle.left(60)
    turtle.forward(10)

cargol()
turtle.done()
