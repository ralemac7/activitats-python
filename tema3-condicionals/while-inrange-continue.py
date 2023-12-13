# Crea un programa que solo haga el cuadrado solo de un numero positivo y si introduce dos veces un numero negativo que termine el programa. 

errors = 0

while True:
    n = float(input("Introduce un número positiu: "))

    if n < 0:
        print("El número ha de ser positiu.")
        errors = errors + 1
        if errors == 2:
            print("Has introduit un número invàlid dues vegades. El programa s'aturarà.")
            break
    else:
        print(f"El quadrat de {n} és {n ** 2}")
        break
