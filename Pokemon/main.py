import random
import combate
import criaturas

def mostrar_barra_progreso(vida, vida_maxima):
    longitud_barra = 20
    progreso_barra = int((vida / vida_maxima) * longitud_barra)
    barra = "[" + "#" * progreso_barra + "-" * (longitud_barra - progreso_barra) + "]" + str(round(vida,1)) + " PS"
    return barra

if __name__ == "__main__":
    
    print("bienvenido al mundo de pokemon!")

    genero = ""

    while genero != "niño" or genero != "niña":
        genero = input("eres un niño o una niña?: ")
        if genero == "niño":
            print("bienvenido")
            break
        elif genero == "niña":
            print("bienvenida!")
            break
        else:
            print("debe escribir niño o niña")
            continue

    edad = input("Que edad tienes?: ")
    if int(edad) < 10:
        if genero == "niño":
            print("no tienes edad para ser entrenador")
        else:
            print("no tienes edad para ser entrenadora")
        quit()

    tipo = ""

    # Elige el pokemon y asigna el tipo y los movimientos a las variables correspondientes
    while True:
        print("\nQue tipo de pokemon quieres para comenzar?\n1 - Fuego\n2 - Planta\n3 - Agua\n4 - Electrico")
        tipo = input("Elige un numero: ")
        if tipo == "3":
            print("\ntu starter es Oshawott")
            jugador = criaturas.crear_pokemon("Oshawott")
            break
        elif tipo == "1":
            print("\ntu starter es Cyndaquil")
            jugador = criaturas.crear_pokemon("Cyndaquil")
            break
        elif tipo == "2":
            print("\ntu starter es Rowlet")
            jugador = criaturas.crear_pokemon("Rowlet")
            break
        elif tipo == "4":
            print("\ntu starter es Pikachu")
            jugador = criaturas.crear_pokemon("Pikachu")
            break
        else:
            print("\nNo tengo ese tipo")

    # Selecciona un pokemon oponente aleatorio
    oponentes = ["Oshawott", "Cyndaquil", "Rowlet", "Pikachu"]
    Oponente = criaturas.crear_pokemon((random.choice(oponentes)))

    # Asiga la vida maxima a las variables de HP
    PS_maximo_jugador = jugador.PS
    PS_maximo_oponente = Oponente.PS

    print("tu oponente es", Oponente.nombre)
    while jugador.PS > 0 and Oponente.PS > 0:
        ataque_jugador = input(f"\nEscoja un ataque: ({jugador.mov1} / {jugador.mov2} / {jugador.mov3})\n")

        # Ataques del jugador
        if ataque_jugador == jugador.mov1 or ataque_jugador == jugador.mov2 or ataque_jugador == jugador.mov3:
            movimiento = ataque_jugador
        else:
            print("¿¿Que estas haciendo?? Debes escojer un ataque disponible!!!")
            continue  # permite al usuario intentar de nuevo

        # efectua el movimiento del jugador
        msg = combate.movimiento(movimiento, jugador, Oponente)
        print(f"\n{jugador.nombre} uso {movimiento}. {msg}")

        if Oponente.PS <= 0:
            Oponente.PS = 0
            break

        # Ataques del oponente
        ataque_oponente = random.randrange(0, 3)
        if ataque_oponente == 0:
            movimiento = Oponente.mov1
        elif ataque_oponente == 1:
            movimiento = Oponente.mov2
        elif ataque_oponente == 2:
            movimiento = Oponente.mov3
        else:
            print("Error en el random")

        # efectua el movimiento del oponente
        msg = combate.movimiento(movimiento, Oponente, jugador)
        print(f"El {Oponente.nombre} oponente uso {movimiento}. {msg}")

        if jugador.PS < 0:
            jugador.PS = 0
        elif Oponente.PS < 0:
            Oponente.PS = 0

        if jugador.PS <= 0:
            jugador.PS = 0
            break

        # Muestra las barras de vida
        print(jugador.nombre + ": " + mostrar_barra_progreso(jugador.PS, PS_maximo_jugador))
        print(Oponente.nombre + " oponente: " + mostrar_barra_progreso(Oponente.PS, PS_maximo_oponente))


    # Final del duelo Pokemon
    if jugador.PS > 0:
        print(jugador.nombre + ": " + mostrar_barra_progreso(jugador.PS, PS_maximo_jugador))
        print(Oponente.nombre + " oponente: " + mostrar_barra_progreso(Oponente.PS, PS_maximo_oponente))

        print(f"\nEl {Oponente.nombre} oponente se ha debilitado.")
        print("Ganaste!")
    else:
        print(jugador.nombre + ": " + mostrar_barra_progreso(jugador.PS, PS_maximo_jugador))
        print(Oponente.nombre + " oponente: " + mostrar_barra_progreso(Oponente.PS, PS_maximo_oponente))

        print(f"\n{jugador.nombre} se ha debilitado.")
        print("Perdiste")
