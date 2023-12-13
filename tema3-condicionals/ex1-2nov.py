while True:
    m = float(input("Introdueix un número: "))
    n = float(input("Introdueix un altre número: "))

    opcio = int(input("""Operacions disponibles:
                  1. Sumar
                  2. Restar
                  3. Multiplicar 
                  
                  Escull una opció: """))
    if opcio == 1:
        print(f"La suma de {m} i {n} és {m + n}.")
        break
    elif opcio == 2:
        print(f"La resta de {m} i {n} és {m - n}.")
        break
    elif opcio == 3:
        print(f"La multiplicació de {m} i {n} és {m * n}.")
        break
    else:
        print("Opció incorrecta.")
        break