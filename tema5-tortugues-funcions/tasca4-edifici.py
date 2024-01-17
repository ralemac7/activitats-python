import turtle

def edifici(pisos, habitacions):
    for i in range(2):
        turtle.fd( 40 * habitacions )
        turtle.lt(90)
        turtle.fd( 40 * pisos )
        turtle.lt(90)
        
    turtle.pu()
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(20)
    turtle.rt(90)

    for i in range(pisos):
        for j in range(habitacions):
            for k in range(2):
                turtle.pd()
                turtle.fd(20)
                turtle.rt(90)
                turtle.fd(10)
                turtle.rt(90)
                turtle.pu()
            turtle.fd(40)
        turtle.bk(40 * habitacions)
        turtle.lt(90)
        turtle.fd(40)
        turtle.rt(90)

edifici(5, 4)
turtle.done()