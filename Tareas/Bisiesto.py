"""
Un año es bisiesto si es divisible entre 4 excepto si es divisible entre 100 y no por 400. Haga el diagrama de flujo de,
e implemente en Visual Studio Code, un programa que reciba como entrada un año entre 1900 y 2199 y además calcule
el número de años bisiestos entre 1900 y el año de entrada (restando de los años posibles todos los que no son bisiestos).

Por ejemplo, el número de años bisiestos hasta 1992 son 23, mientras que el de 2199 son 93.

Recuerde que // da el cociente de la división y % da el residuo

Debe implementar dos versones del programa: una que use ciclos, y una que no los use.
"""

# VERSION DE CICLOS

year = input("Ingresa un año entre 1900 y 2199: ")

while True:
    if year.isnumeric():
        year = float(year)
        if year <= 1900 or year >= 2199:
            print("Debes ingresar un numero mayor a 1900 o menor a 2199. Por favor vuelve a intentarlo. /n")
            year = input("Ingresa un año: ")
        else:
            break
    else:
        print("Debes ingresar un numero. Por favor vuelve a intentarlo. /n")
        year = input("Ingresa un año: ")

contador = 0

if year > 1900 and year < 2199:
    year = int(year)
    for i in range(1900, year + 1):
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            contador += 1

print(f"Entre el año {year} y el año 2199 hay {contador} años bisiestos.")
