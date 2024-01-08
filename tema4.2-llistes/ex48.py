# Volem emmagatzemar la temperatura mínima i màxima de 5 dies. 
# Realitza un programa que doni la següent informació:
# La temperatura de cada dia
# Els dies que la mínima està per sota de la mitjana.
# Que el programa llegeixi una temperatura per teclat i indiqui
# quins dies coincideixin amb la temperatura màxima. I si no hi ha cap, que mostri un missatge.

tempsmin = []
tempsmax = []

for i in range(1, 6):
    tempmin = float(input(f"Introdueix la temperatura mínima per al dia {i}: "))
    tempmax = float(input(f"Introdueix la temperatura màxima per al dia {i}: "))
    tempsmin.append(tempmin)
    tempsmax.append(tempmax)

mitjanatempmin = sum(tempsmin) / len(tempsmin)

for i in range(5):
    print(f"Dia {i+1}: Temperatura mínima = {tempsmin[i]}ºC, Temperatura màxima = {tempsmax[i]}ºC")

print("Dies on la temperatura mínima està per sota de la mitjana:")
for i in range(5):
    if tempsmin[i] < mitjanatempmin:
        print(f"Dia {i+1}")

temp = float(input("Introdueix una temperatura: "))
diescoincidents = []
for i in range(5):
    if tempsmax[i] == temp:
        diescoincidents.append(i+1)

if diescoincidents:
    print(f"La temperatura introduïda és la temperatura màxima els dies: {diescoincidents}")
else:
    print("La temperatura introduïda no és la temperatura màxima cap dia.")