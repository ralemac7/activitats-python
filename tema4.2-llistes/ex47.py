# Es necessita fer un programa per la matèria d’estadística que demani una sèrie de números 
# separats per una coma i després calculi la seva mitjana i la seva desviació típica.

inpNumeros = str(input("Introdueix números separats per una coma, per exemple (2,5,7,9,3,4,7): "))
numeros = [int(numeros) for numeros in inpNumeros.split(",")]

mitjana = sum(numeros) / len(numeros)
varianca = sum((x - mitjana) ** 2 for x in numeros) / len(numeros)
desviacio_tipica = varianca ** 0.5

print(f"Has introduit els numeros: {numeros}")
print(f"La varianca és {round(varianca, 4)}")
print(f"La desviación típica es {round(desviacio_tipica, 4)}")