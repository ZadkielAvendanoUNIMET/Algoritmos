"""
Una famosa cadena de cines en Venezuela te contrató para hacerles un programa de descuento
en las entradas basado en la edad del cliente, para ello tendrás que recibir por teclado la edad y
nombre del cliente y verificar los siguientes casos:

a. Si su edad es menor o igual a 4 años el precio de su entrada es gratis.
b. Si su edad es menor o igual a 18 años el precio de su entrada es de $1.50
c. Si su edad es mayor o igual a los 60 años su entrada tendrá un valor de $1
d. La entrada para un adulto promedio es de $2.00

Deberás imprimir un mensaje dependiendo de la edad del cliente para saber el precio de su
entrada.

Output: 'El cliente: {nombre} tiene: {edad} años y su entrada de cine cuesta: ${precio_entrada}'
"""

nombre = input("Nombre del cliente: ")
edad = input("Ingresa tu edad: ")
edad = float(edad)

if edad <= 4:
    precio_entrada = "Gratis"
elif edad <= 18:
    precio_entrada = "$1.50"
elif edad >= 60:
    precio_entrada = "$1"
else:
    precio_entrada = "$2"

edad = str(int(edad))
print("El cliente:", nombre, "tiene:", edad, "años y su entrada de cine cuesta:", precio_entrada)