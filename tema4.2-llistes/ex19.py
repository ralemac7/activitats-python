# Una tutora necessita un minipgroama que pugui imprimir el llistat del seu grup en pantalla.
# A més, també necessita tenr al menú tres opcions: poder afegir un nou alumne a la posició que vulgui,
# també substituir qualsevol nom i comprovar quants registres té la llista.

alumnes = ["Joan", "Maria", "Carles", "Laia", "Pere", "Anna", "Lluc", "Sofia", "Miquel", "Lucia"]

while True:
    opcio = float(input("""Opcions disponibles:
    1) Veure la llista
    2) Afegir un alumne
    3) Substituir un alumne
    4) Finalitzar el programa

    La teva elecció: """))

    if opcio == 1:
        print(f"Els alumnes a la llista de classe són: {alumnes}")
        print(f"Hi ha un total de {len(alumnes)}")
    elif opcio == 2:
        nomAlumne = str(input("Introdueix el nom de l'alumne que vols afegir: "))
        numLlista = int(input("Introdueix a quina posició de la llista vols afegir a l'alumne: "))
        alumnes.insert(numLlista, nomAlumne)
        print(f"L'alumne {nomAlumne} ha sigut afegit a la llista de classe a la posició {numLlista}.")
    elif opcio == 3:
        nomAlumne = str(input("Introdueix el nom de l'alumne que vols substituir: "))
        numLlista = int(input("Introdueix a quina posició de la llista vols substituir a l'alumne: "))
        alumnes[numLlista] = nomAlumne
        print(f"L'alumne {nomAlumne} ha sigut substituit a la llista de classe a la posició {numLlista}.")
    elif opcio == 4:
        print("Aturant programa...")
        break
    else:
        print("Has introduït una opció invàlida. Comprova la teva elecció i torna a intentar-ho.")