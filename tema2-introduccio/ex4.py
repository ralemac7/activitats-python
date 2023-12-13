# Estabas acampando con tus amigos lejos de casa, pero cuando llega el momento de regresar,
# ¡te das cuenta de que se te está acabando el combustible y que el surtidor más cercano está a 50 km de distancia!
# Sabes que, en promedio, tu automóvil funciona con aproximadamente 25 km por litro. Quedan 2 litros.
# Teniendo en cuenta estos factores, escribe una función que te diga si es posible llegar a la gasolinera o no. 
# La función debe devolver verdadero si es posible y falso si no.

litrosGasolina = float(input("Introduce cuántos litros de gasolina te quedan: "))

if litrosGasolina > 0:
    kmRestantes = ( litrosGasolina * 25 )
    print(f"Con {litrosGasolina}L podrás recorrer {kmRestantes}km.")
    if kmRestantes >= 50:
        print("No te preocupes, llegarás a la gasolinera.")
    else:
        print("No llegarás a la gasolinera, deberás rellenar el depósito antes.")
else:
    print("Has introducido un valor inválido, por favor, revisa el valor introducido.")