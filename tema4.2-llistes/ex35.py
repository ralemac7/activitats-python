# Escriu un porgrama amb una llista predefinida amb alguns valors duplicats i que surti en pantalla la mateixa
# llista però sense els valors duplicats i ordenada alfabeticament.
#
# Pista: pots traspassar els valors d'una llista a una altra llista.
#
# ["Joan", "Pere", "Lucia", "Maria", "Carles", "Laia", "Pere", "Anna", "Lluc", "Sofia", "Joan", "Miquel", "Lucia"]

alumnes = []
alumnesSenseDuplicar = []

for i in range(int(input("Quants alumnes vols afegir? "))):
    alumne = str(input("Introdueix el nom de l'alumne: "))
    alumnes.append(alumne)

for i in alumnes:
    if i not in alumnesSenseDuplicar:
        alumnesSenseDuplicar.append(i)

print(f"""
Alumnes desordenats (i possiblement duplicats):
    - {alumnes}
Alumnes ordenats (i sense duplicar):
    - {sorted(alumnesSenseDuplicar)}
""")
