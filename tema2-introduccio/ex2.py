jugadaPersona1 = int(input("""
    Jugadas disponibles:
                           1. Piedra
                           2. Papel
                           3. Tijera
                           
                           Escoge una opción: """))
jugadaPersona2 = int(input("""
    Jugadas disponibles:
                           1. Piedra
                           2. Papel
                           3. Tijera
                           
                           Escoge una opción: """))

if jugadaPersona1 == jugadaPersona2:
    ganador = "ninguno"

elif jugadaPersona1 == 1 and jugadaPersona2 == 2:
    ganador = "persona 2"
elif jugadaPersona1 == 1 and jugadaPersona2 == 3:
    ganador = "persona 1"
elif jugadaPersona1 == 2 and jugadaPersona2 == 1:
    ganador = "persona 1"
elif jugadaPersona1 == 2 and jugadaPersona2 == 3:
    ganador = "persona 2"
elif jugadaPersona1 == 3 and jugadaPersona2 == 1:
    ganador = "persona 2"
elif jugadaPersona1 == 3 and jugadaPersona2 == 2:
    ganador = "persona 1"

print(f"Ganador: {ganador}")