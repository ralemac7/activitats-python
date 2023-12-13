notes = []

while True:
    opcio = int(input("""Opcions disponibles:
1) Veure llistat de notes
2) Afegir nota
3) Eliminar una nota
4) Eliminar llistat de notes
5) Finalitzar programa

La teva elecció: """))
    if opcio == 1:
        if len(notes) == 0:
            print("Encara no hi han notes afegides. Pots afegir-ne una amb l'opció 2.")
        else:
            print(f"Les notes afegides són: {notes}")
    elif opcio == 2:
        for i in range(int(input("Introdueix quantes notes vols afegir: "))):
            nota = float(input("Introdueix la nota que vols afegir: "))
            if nota > 10:
                print("La nota no pot excedir el 10. Intenta-ho de nou (1/3)")
                nota = float(input("Introdueix la nota que vols afegir: "))
                if nota > 10:
                    print("La nota no pot excedir el 10. Intenta-ho de nou (2/3)")
                    nota = float(input("Introdueix la nota que vols afegir: "))
                    if nota > 10:
                        print("Has introduït una nota invàlida 3 vegades. Saltant aquesta posició")
                    else:
                        notes.append(nota)
                        print(f"S'ha afegit la nota {nota} al llistat de notes.")
                else:
                    notes.append(nota)
                    print(f"S'ha afegit la nota {nota} al llistat de notes.")
            else:
                notes.append(nota)
                print(f"S'ha afegit la nota {nota} al llistat de notes.")
    elif opcio == 3:
        pos = int(input(f"Introdueix la posició de la nota que vols eliminar (0-{( len(notes) - 1 )}): "))
        if pos > len(notes):
            print("Aquesta nota no està registrada encara.")
        else:
            del(notes[pos])
            print(f"S'ha eliminat la nota {nota} del llistat de notes.")
    elif opcio == 4:
        notes = []
        print("S'ha esborrat el llistat de notes.")
    elif opcio == 5:
        print("Aturant el programa...")
        break
    else:
        print("Opció invàlida. Torna-ho a intentar.")