# Volem guardar els noms i edats dels alumnes d’un curs. Realitza un programa que es pugui introduir el nom i l’edat de cada alumne.
# El procés de lectura de dades termina quan s'introdueix com a nom un asterisc (*). Al finalitzar s’haurà de mostrar les següents dades:
# Tots els alumnes majors d’edat
# L’alumne que té major edat

estudiants = []
edats = []

while True:
    nom = input("Introdueix el nom de l'estudiant: ")
    if nom != "*":
        estudiants.append(nom)
        edat = int(input("Introdueix l'edat de l'estudiant: "))
        edats.append(edat)
    else:
        edatMaxima = max(edats)
        for estudiant, edat in zip(estudiants, edats):
            print(f"L'estudiant {estudiant} té {edat} anys.")
            if edat >= 18:
                print(f"L'estudiant {estudiant} és major d'edat.")
            if edat == edatMaxima:
                print(f"L'estudiant {estudiant} és el més major.")
        break