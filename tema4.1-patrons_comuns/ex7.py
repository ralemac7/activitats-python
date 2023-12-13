# A un campionat de futbol, tots els equips han de jugar entre ells dos vegades, una com local
# i l'altre com a visitant. Evidentment, cap dels equips poden jugar amb ells mateixos i per tant cal excloure
# aquests casos. Crea un programa on es reculli aquests partiits tenint en compte que hi ha 6 equips que estan
# numerats de l'1 al 6.

print("Partits possibles entre els 6 equips:")

for local in range(1, 6 + 1):
    for visitant in range(local + 1, 6 + 1):
        print(f"Local: {local} |  Visitant: {visitant}")
