def calcular_import_total(dies_lloguer):
    preu_per_dia = 40
    descompte_7_dies = 50
    descompte_3_dies = 20

    import_total = dies_lloguer * preu_per_dia

    if dies_lloguer >= 7:
        import_total -= descompte_7_dies
    elif dies_lloguer >= 3:
        import_total -= descompte_3_dies

    return import_total


def calcul(dies_lloguer):
    gasolina = 100
    peatges = 50

    import_total = calcular_import_total(dies_lloguer)

    print("El import total sense gasolina i peatges es de", import_total, "euros")

    diposit_ple = input("El diposit esta ple? (S/N): ")
    if diposit_ple == "S":
        import_total -= gasolina
        print("El import total amb gasolina es de", import_total, "euros")
    else:
        print("El import total sense gasolina es de", import_total, "euros")

    peatges_passats = int(input("Quants peatges heu passat durant el lloguer?: "))
    import_total -= peatges
    import_total -= peatges_passats

    print("El import total amb peatges es de", import_total, "euros")

    if diposit_ple == "S":
        retorn_gasolina = 100
    else:
        retorn_gasolina = 0

    retorn_peatges = 50 - peatges_passats
    if retorn_peatges < 0:
        retorn_peatges = 0

    print("El total a retornar es de", retorn_gasolina + retorn_peatges, "euros")