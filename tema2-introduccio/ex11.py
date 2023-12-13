num = int(input("Introduce el número del cual quieres obtener su tabla de multiplicación: "))

for i in range (1, 11):
    print(f"{num}x{i} = {num * i}")