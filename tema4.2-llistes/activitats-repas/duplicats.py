# Duplicats: pomes, llet
llista_compra = ["pomes", "llet", "ous", "pomes", "llet"]
llista_sense_duplicar = []

for i in llista_compra:
    if i not in llista_sense_duplicar:
        llista_sense_duplicar.append(i)

print(llista_compra)
print(llista_sense_duplicar)
print(sorted(llista_sense_duplicar))
print(sorted(llista_sense_duplicar, reverse=True))