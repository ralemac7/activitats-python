a = 0
b = 1

for i in range(98):
    r = a + b
    a = b
    b = r
    print(r)
