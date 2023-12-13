v1 = []
v2 = []

dimensio = int(input("Quantes dimensions tenen els vectors a calcular? "))

print("Introdueix les dades del vector 1:")
for i in range(1, ( dimensio + 1 )):
    v1.append(float(input(f"Introdueix el valor de la dimensió {i}: ")))
print("Introdueix les dades del vector 2:")
for i in range(1, ( dimensio + 1 )):
    v2.append(float(input(f"Introdueix el valor de la dimensió {i}: ")))

prodEsc = 0
for x, y in zip(v1, v2):
    prodEsc += x * y

print(f"Producte escalar (v1, v2): {prodEsc}")