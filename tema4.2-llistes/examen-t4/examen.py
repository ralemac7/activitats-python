# D'una empressa de transports es vol guardar el nom dels conductors que té i 
# els kilometres que condueixen cada dia de la setmana.
# Per guardar aquesta informació es necessita tenir les següents coses:
# Noms: és la llista per guardar els conductors 
# kms: és la llista per guardar els kilometres de cada dia de la setmana 
# dies: és la llista pels dies de la setmana 
# total_km: és la llista per guardar el total de kilometres per dia
# mit_dia: és la llista per guardar la mitjana de km per dia
# mit_con: és la mitjana per guardar la mitjana de km de la setmana del conductor
# Al finalitzar s'ha de mostrar una llista amb tots els
# noms dels conductors i els kilometres totals realitzats per cadascun. 

# Per exemple: "En Joan ha fet 35km en tota la setmana" També ha de mostrar la mitjana de kilometres fets al dia i una
# mitjana de kilometres fets per cada conductor. Per exemple: "La mitjana de kilometres el dilluns és 25,4 km" i "La mitjana de kilometres
# en tota la setmana d'en Joan és de 34,7 km" En el cas que puguis o vulguis millorar aquest programa, fes la 
# proposta
#
# User: RLM
# Password: 569 

treballadors = ["Carles", "Robert", "Arnau"]
kilometres = []
total_km = []
mit_dia = []
mit_con = []

while True:
    opcio = int(input("""Opcions disponibles:
                      1) Afegir treballadors
                      2) Afegir kilometres
                      3) Veure informe
                      4) Finalitzar programa
                      
                      Escull una opció: """))
    
    if opcio == 1:
        quantAfegir = int(input("Quants treballadors vols afegir? "))
        for i in range(quantAfegir):
            treballadorAfegir = str(input(f"Introdueix el nom del treballador {i}: "))
            treballadors.append(treballadorAfegir)
            print(f"S'ha afegit al treballador {treballadorAfegir}")
        print(f"Els treballadors de la llista actualment són: {treballadors}")
    elif opcio == 2:
        print(len(treballadors))
        for i in range(len(treballadors)):
            km_semana = []
            print(f"Introduint dades del treballador {treballadors[i]}")
            for i in range(1, 8):
                km_dia = float(input(f"Introdueix quants quilometres ha fet al dia {i} de la setmana: "))
                km_semana.append(km_dia)
            kilometres.append(km_semana)
        print(kilometres)
    elif opcio == 3:
        print("Kilometres per treballador i dia:")
        for treballadors, kilometres in zip(treballadors, kilometres):
            print(treballadors, kilometres)
    elif opcio == 4:
        print("Aturant el programa...")
        break
    else:
        print("Opció invàlida. Torna-ho a intentar.")