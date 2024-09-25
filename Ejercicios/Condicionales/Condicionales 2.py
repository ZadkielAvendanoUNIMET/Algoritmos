# Dadas tres variables enteras a, b y c con valores diferentes, determinar cuál es la suma máxima de dos de esas variables

a, b, c = (6, 7, 9)

suma_1 = a + b
suma_2 = a + c
suma_3 = b + c

print("La suma maxima es", max(suma_1, suma_2, suma_3))