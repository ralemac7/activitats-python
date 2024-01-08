# Escriu un programa que permeti 
# multiplicar únicament les matrius
# de 2 files per 2 columnes.

A = [[6, -7], [4, 2]]
B = [[3, 7], [-8, 2]]

result = [[0, 0], [0, 0]]

result[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
result[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
result[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
result[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]

print(result)