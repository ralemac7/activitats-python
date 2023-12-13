c = 0

for i in range(1000):
    ultimoNum = (i ** 3) % 10
    if ultimoNum == 7:
        c = c + 1

print(c)