vuela = str(input("¿Vuela? (s/n): "))
esHumano = str(input("¿Es humano? (s/n): "))
tieneMascara = str(input("¿Tiene máscara? (s/n): "))

if vuela == "s":
    if esHumano == "s":
        if tieneMascara == "s":
            print("El personaje es Iron Man")
        else:
            print("El personaje es Capitan Marvel.") 
    else:
        if tieneMascara == "s":
            print("El personaje es Ronan Acusser.")
        else:
            print("El personaje es Vision.")
else:
    if esHumano == "s":
        if tieneMascara == "s":
            print("El personaje es Spiderman")
        else:
            print("El personaje es Hulk.")
    else:
        if tieneMascara == "s":
            print("El personaje es Thanos.")
        else:
            print("El personaje es Groot.")