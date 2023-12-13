print("Introduce 10 números positivos:")

menor = 1
mayor = -1

for i in range(10):
    n = int(input("- "))
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n
    print(f"El máximo es {mayor} y el menor {menor}.")