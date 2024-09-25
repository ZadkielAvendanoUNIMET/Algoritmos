# Realizar un programa donde se reciba un número flotante por teclado e imprima un mensaje diciendo si el número es par o impar y evaluar si es positivo/negativo

n = input("Ingresa un numero: ")
n = float(n)

if n == 0:
    print("Ingresa un numero que no sea igual a 0.")
    quit()
elif n > 0:
    signo = "positivo"
elif n < 0:
    signo = "negativo"
else:
    print("Ingresa un numero valido.")
    quit()

if (n % 2) == 0:
    par_impar = "par"
else:
    par_impar = "impar"

print("El número: " + str(int(n)) + " es " + par_impar + " y " + signo)