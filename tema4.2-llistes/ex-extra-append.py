compra = []
print(f"Actualment hi han els seguents elements a la llista: {compra}")
for i in range(int(input("Quants elements vols afegir a la llista? "))):
    compra.append(str(input("Que vols afegir: ")))
veureLlista = str(input("Vols veure la llista? (S/N): "))
if veureLlista == "S":
    print(compra)
else:
    print("Has introduit no o una opció invàlida, aturant, gràcies.")