valors = "32, 25, 14, 8, 24, 96"
llistavalors = [int(valors) for valors in valors.split(", ") if valors.startswith("2")]

print(llistavalors)