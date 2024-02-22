# Examen Python Unitat 4.2 - Llistes

# Un concessionari de cotxes necessita realitzar un inventari de ventes de cotxes durant tot un any.
# Aquest inventari ha de tenir el registre del numero de cotxes que es venen mensualment dels 5 tipus de model (Bàsic, Familiar, Tot-terreny, Deportiu i Furgoneta)
# Per guardar aquesta informació es necessita tenir les següents coses:
#
#    Models: és la llista per guardar els models.
#    vendes: és la llista per guardar les ventes de cada mes de l'any
#    mesos: és la llista pels mesos de la setmana
#    total_vendes: és la llista per guardar el total de ventes per any
#    mit_mes: és la llista per guardar la mitjana de ventes per mes
#
# Al finalitzar s'ha de mostrar una llista amb tots els mesos amb les ventes totals de cada mes.
# Per exemple: "Al març es van vendre 58 cotxes de tots els models"
# També ha de mostrar la mitjana mensual
# Per exemple: "La mitjana de cotxes venuts al mes és de 84 cotxes)
# I per últim, el total de cotxes venuts de cada model durant l'any.
# Per exemple: "S'han venut 35 cotxes del model Bàsic", "S'han venut 12 cotxes del model Familiar", etc...

import time

models = ["Bàsic", "Familiar", "Tot-terreny", "Deportiu", "Furgoneta"]
vendesBasic = []
vendesFamiliar = []
vendesTotTerreny = []
vendesDeportiu = []
vendesFurgoneta = []

for mes in range(1, 13):
    if mes == 1:
        nomMes = "Gener"
    elif mes == 2:
        nomMes = "Febrer"
    elif mes == 3:
        nomMes = "Març"
    elif mes == 4:
        nomMes = "Abril"
    elif mes == 5:
        nomMes = "Maig"
    elif mes == 6:
        nomMes = "Juny"
    elif mes == 7:
        nomMes = "Juliol"
    elif mes == 8:
        nomMes = "Agost"
    elif mes == 9:
        nomMes = "Septembre"
    elif mes == 10:
        nomMes = "Octubre"
    elif mes == 11:
        nomMes = "Novembre"
    elif mes == 12:
        nomMes = "Desembre"
    print(f"\nVendes de cotxes del mes de {nomMes}:\n")
    for model in range(1, 6):
        if model == 1:
            vendes = int(input(f"Quants cotxes del model Bàsic s'han venut al mes de {nomMes}? "))
            vendesBasic.append(vendes)
        elif model == 2:
            vendes = int(input(f"Quants cotxes del model Familiar s'han venut al mes de {nomMes}? "))
            vendesFamiliar.append(vendes)
        elif model == 3:
            vendes = int(input(f"Quants cotxes del model Tot-terreny s'han venut al mes de {nomMes}? "))
            vendesTotTerreny.append(vendes)
        elif model == 4:
            vendes = int(input(f"Quants cotxes del model Deportiu s'han venut al mes de {nomMes}? "))
            vendesDeportiu.append(vendes)
        elif model == 5:
            vendes = int(input(f"Quants cotxes del model Furgoneta s'han venut al mes de {nomMes}? "))
            vendesFurgoneta.append(vendes)
print(vendes)
while True:
    opcio = int(input("""Quines dades estadístiques vols veure?
1) Vendes de cotxes per mesos
2) Mitjana de cotxes venuts al mes
3) Total de cotxes venuts de cada model durant l'any

Per sortir, prem 0
La teva selecció: """))
    if opcio == 0:
        print("\nTancant programa...")
        time.sleep(1)
        break
    elif opcio == 1:
        print(f"""
Vendes de cotxes per mesos:
- Gener: {vendesBasic[0] + vendesFamiliar[0] + vendesTotTerreny[0] + vendesDeportiu[0] + vendesFurgoneta[0]} cotxes
- Febrer: {vendesBasic[1] + vendesFamiliar[1] + vendesTotTerreny[1] + vendesDeportiu[1] + vendesFurgoneta[1]} cotxes
- Març: {vendesBasic[2] + vendesFamiliar[2] + vendesTotTerreny[2] + vendesDeportiu[2] + vendesFurgoneta[2]} cotxes
- Abril: {vendesBasic[3] + vendesFamiliar[3] + vendesTotTerreny[3] + vendesDeportiu[3] + vendesFurgoneta[3]} cotxes
- Maig: {vendesBasic[4] + vendesFamiliar[4] + vendesTotTerreny[4] + vendesDeportiu[4] + vendesFurgoneta[4]} cotxes
- Juny: {vendesBasic[5] + vendesFamiliar[5] + vendesTotTerreny[5] + vendesDeportiu[5] + vendesFurgoneta[5]} cotxes
- Juliol: {vendesBasic[6] + vendesFamiliar[6] + vendesTotTerreny[6] + vendesDeportiu[6] + vendesFurgoneta[6]} cotxes
- Agost: {vendesBasic[7] + vendesFamiliar[7] + vendesTotTerreny[7] + vendesDeportiu[7] + vendesFurgoneta[7]} cotxes
- Setembre: {vendesBasic[8] + vendesFamiliar[8] + vendesTotTerreny[8] + vendesDeportiu[8] + vendesFurgoneta[8]} cotxes
- Octubre: {vendesBasic[9] + vendesFamiliar[9] + vendesTotTerreny[9] + vendesDeportiu[9] + vendesFurgoneta[9]} cotxes
- Novembre: {vendesBasic[10] + vendesFamiliar[10] + vendesTotTerreny[10] + vendesDeportiu[10] + vendesFurgoneta[10]} cotxes
- Desembre: {vendesBasic[11] + vendesFamiliar[11] + vendesTotTerreny[11] + vendesDeportiu[11] + vendesFurgoneta[11]} cotxes""")
        print("Tornant al menú principal en 5 segons...\n")
        time.sleep(5)
    elif opcio == 2:
        mitjana = (sum(vendesBasic) + sum(vendesFamiliar) + sum(vendesTotTerreny) + sum(vendesDeportiu) + sum(vendesFurgoneta)) / 12
        print(f"\nLa mitjana de cotxes venuts al mes és de {mitjana} cotxes")
        print("Tornant al menú principal en 2 segons...\n")
        time.sleep(2)
    elif opcio == 3:
        print(f"""
Total de cotxes venuts de cada model durant l'any:
- Bàsic: {sum(vendesBasic)} cotxes
- Familiar: {sum(vendesFamiliar)} cotxes
- Tot-terreny: {sum(vendesTotTerreny)} cotxes
- Deportiu: {sum(vendesDeportiu)} cotxes
- Furgoneta: {sum(vendesFurgoneta)} cotxes""")
        print("Tornant al menú principal en 5 segons...\n")
        time.sleep(5)
    else:
        print("\nOpció incorrecta. Torna a intentar-ho.\n")
        time.sleep(1)