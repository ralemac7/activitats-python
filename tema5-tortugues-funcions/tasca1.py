import turtle
import random

tortuga = turtle.Turtle()

tortuga.pensize(5)
tortuga.color("#FE5000")

numCostats = int(input("Introdueix de quants costats vols dibuixar el poligon (Introdueix 0 per número de costats aleatoris): "))

if numCostats == 0:
    numCostats = random.randint(1, 10)
    print(f"Es fará un polígon de {numCostats} costats.")

angle = ( 360 / numCostats)

for i in range(numCostats):
    tortuga.forward(100)
    tortuga.right(angle)

tortuga.goto(-100, 50)
tortuga.backward(100)

tortuga.penup()

tortuga.right(90)
tortuga.forward(50)
tortuga.left(90)

tortuga.pendown()

for i in range(numCostats):
    tortuga.forward(100)
    tortuga.right(angle)

turtle.done()