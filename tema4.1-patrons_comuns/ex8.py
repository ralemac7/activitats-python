import math

n = int(input("Introdueix un número: "))
m = int(input("Introdueix un altre número: "))

print(f"Màxim comú divisor: {math.gcd(n, m)}")
print(f"Mínim comú múltiple: {math.lcm(n, m)}")