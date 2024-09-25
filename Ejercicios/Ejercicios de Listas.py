#Suponga una lista de 100 números que representan las notas de un grupo de estudiantes, realice un algoritmo que determine:
# a. El promedio de notas del salón
# b. Cuántos alumnos aprobaron
# c. Cuántos alumnos reprobaron

notas = [5, 12, 3, 19, 8, 14, 7, 1, 20, 6, 11, 18, 2, 9, 15, 4, 13, 10, 17, 16, 5, 12, 3, 19, 8, 14, 7, 1, 20, 6, 11, 18, 2, 9, 15, 4, 13, 10, 17, 16, 5, 12, 3, 19, 8, 14, 7, 1, 20, 6, 11, 18, 2, 9, 15, 4, 13, 10, 17, 16, 5, 12, 3, 19, 8, 14, 7, 1, 20, 6, 11, 18, 2, 9, 15, 4, 13, 10, 17, 16, 5, 12, 3, 19, 8, 14, 7, 1, 20, 6, 11, 18, 2, 9, 15, 4, 13, 10, 17, 16]

promedio = 0
alumnos_aprobados = 0

# a)

promedio = sum(notas) / len(notas)

print("El promedio de las notas es: " + str(promedio))

# b)

notas = sorted(notas)

for i in notas:
    if i >= 10:
        alumnos_aprobados += 1

print("Alumnos aprobados: " + str(alumnos_aprobados))

# c)

print("Alumnos reprobados: " + str(len(notas) - alumnos_aprobados))