dia = int(input("Introdueix el día del mes (1-31)): "))
mes = int(input("Introdueix el mes del año (1-12): "))

if dia == 1 or dia == 8 or dia == 15 or dia == 22 or dia == 29:
    diaSemana = "lunes"
elif dia == 2 or dia == 9 or dia == 16 or dia == 23 or dia == 30:
    diaSemana = "martes"
elif dia == 3 or dia == 10 or dia == 17 or dia == 24 or dia == 31:
    diaSemana = "miércoles"
elif dia == 4 or dia == 11 or dia == 18 or dia == 25:
    diaSemana = "jueves"
elif dia == 5 or dia == 12 or dia == 19 or dia == 26:
    diaSemana = "viernes"
elif dia == 6 or dia == 13 or dia == 20 or dia == 27:
    diaSemana = "sábado"
elif dia == 7 or dia == 14 or dia == 21 or dia == 28:
    diaSemana = "domingo"
else:
    diaSemana = "inválido"

if mes == 1:
    mesAño = "enero"
elif mes == 2:
    mesAÑo = "febrero"
elif mes == 3:
    mesAño = "marzo"
elif mes == 4:
    mesAño = "abril"
elif mes == 5:
    mesAño = "mayo"
elif mes == 6:
    mesAño = "junio"
elif mes == 7:
    mesAño = "julio"
elif mes == 8:
    mesAño = "agosto"
elif mes == 9:
    mesAño = "septiembre"
elif mes == 10:
    mesAño = "octubre"
elif mes == 11:
    mesAño = "noviembre"
elif mes == 12:
    mesAño = "diciembre"
else:
    mesAño = "inválido"



if diaSemana == "inválido" or mesAño == "inválido":
    print("Has introducido un día o mes inválido. Los días pueden ser entre 1-31 y los meses entre 1-12.")
else:
    print(f"Hoy es {diaSemana}, {dia} de {mesAño}.")