grup = []

while True:
    opcio = int(input("""Opcions disponibles:
                      1) Veure el llistat d'alumnes
                      2) Afegir un nou alumne al llistat
                      3) Substituir un alumne del llistat
                      4) Comprovar el numero d'alumnes al llistat
                      5) Finalitzar el programa
                      
                      Opció escollida: """))
    
    if opcio == 1:
        print("Alumnes del llistat:")
        print(grup)
    elif opcio == 2:
        alumneAfegir = str(input("Quin es el nom de l'alumne a afegir? "))
        posicioAfegir = int(input("A quina posició del llistat vols afegir a l'alumne? "))
        grup.insert(posicioAfegir, alumneAfegir)
        print(f"S'ha afegit a {alumneAfegir} a la posició {posicioAfegir} del llistat.")
    elif opcio == 3:
        alumneSubstituir = str(input("Quin es el nom del nou alumne que vols posar al llistat? "))
        posicioSubstituir = int(input("A quina posició del llistat vols que es substitueixi? "))
        alumneVell = grup[posicioSubstituir]
        grup[posicioSubstituir] = alumneSubstituir
        print(f"S'ha substituit l'alumne {alumneVell} per {alumneSubstituir} a la posició {posicioSubstituir} del llistat.")
    elif opcio == 4:
        print(f"Hi han {len(grup)} alumnes al llistat del grup.")
    elif opcio == 5:
        print("Finalitzant el programa...")
        break
    else:
        print("Has introduit una opció invàlida! Intenta-ho de nou.")