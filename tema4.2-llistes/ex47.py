# Es necessita fer un programa per la matèria d’estadística que demani una sèrie de números 
# separats per una coma i després calculi la seva mitjana i la seva desviació típica.

inpNumeros = str(input("Introdueix números separats per una coma i un espai, per exemple (2, 5, 7, 3): "))

numeros = [int(numeros) for numeros in inpNumeros.split(", ")]

mitjana = ( sum(numeros) / len(numeros) )
suma_diferencies = sum((num - mitjana) ** 2 for num in numeros)
desviacio_tipica = (suma_diferencies / len(numeros)) ** 0.5

print(f"La mitjana dels números introduits és de {mitjana}.")
print(f"La desviació típica és de {round(desviacio_tipica, 4)}")
