print("Introdueix 10 numeros positius:")

mayor = -1

for i in range(10):
    n = int(input("- "))
    if n > mayor:
        mayor = n
    print(f"El mayor es {mayor}.")