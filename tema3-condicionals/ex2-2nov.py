from math import sin, cos, tan

for i in range(1, 31):
    if i % 10 == 7:
        print(f"Saltant el valor {i} perquè acaba en 7.")
    print(f"Del número {i} el sinus és {round(sin(i), 4)}, el cosinus és {round(cos(i), 4)} i la tangent és {round(tan(i), 4)}.")