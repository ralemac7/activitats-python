import random

errores = 0
numAleatorio = random.randrange(1 , 5)

debug = str(input("¿Habilitar debug? (S/N): "))

if debug == "S":
    print(f"El número aleatorio es {numAleatorio}.")

while True:
    numIntroducido = int(input("Adivina el número entre 1 y 5: "))
    if numIntroducido < 1 or numIntroducido > 5:
        print(f"¡Debes de introducir un número entre 1 y 5!")
    elif numIntroducido != numAleatorio:
        errores = errores + 1
        print(f"El número introducido no es el correcto. Llevas {errores} intentos.")
    else:
        print(f"¡Enhorabuena! Has adivinado el número {numAleatorio} en {errores} intentos")
        break