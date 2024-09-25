import random

def mostrar_barra_progreso(vida, vida_maxima):
    longitud_barra = 20
    progreso_barra = int((vida / vida_maxima) * longitud_barra)
    barra = "[" + "#" * progreso_barra + "-" * (longitud_barra - progreso_barra) + "]"
    return barra

print("bienvenido al mundo de pokemon!")
genero = input("eres un niño o una niña?: ")

if genero == "niño":
    print("bienvenido")
elif genero == "niña":
    print("bienvenida!")
else:
    print("debe escribir niño o niña")
    quit()

edad = input("Que edad tienes?: ")
if int(edad) < 10:
    if genero == "niño":
        print("no tienes edad para ser entrenador")
    else:
        print("no tienes edad para ser entrenadora")
    quit()

print("Comienza tu aventura!")
region = input("Necesitarás un compañero de viaje. En qué región te encuentras? ")
if region == "kanto" and genero == "niño":
    print("tu compañera de viaje es misty")
else:
    print("tu compañero de viaje es brook")

tipo = ""

# Elige el pokemon y asigna el tipo y los movimientos a las variables correspondientes
while tipo != "fuego" or tipo != "planta" or tipo != "agua":
   tipo = input("Qué tipo de pokemon quieres para comenzar? (agua / fuego / planta): ")
   if tipo == "agua":
      print("tu starter es Oshawott")
      Pokemon = "Oshawott"
      movimiento_especial = "hidro pulso"
      tipo_jugador = "agua"
      break
   elif tipo == "fuego":
      print("tu starter es Cyndaquil")
      Pokemon = "Cyndaquil"
      movimiento_especial = "ascuas"
      tipo_jugador = "fuego"
      break
   elif tipo == "planta":
      print("tu starter es Rowlet")
      Pokemon = "Rowlet"
      movimiento_especial = "hoja afilada"
      tipo_jugador = "planta"
      break
   else:
      print("No tengo ese tipo")

# Selecciona un pokemon oponente aleatorio
oponentes = [("Oshawott", "hidro pulso", "agua"), ("Cyndaquil", "ascuas", "fuego"), ("Rowlet", "hoja afilada", "planta")]
oponente, movimiento_especial_oponente, tipo_oponente = random.choice(oponentes)
print("tu oponente es", oponente)

PS_jugador = 150
PS_oponente = 150
defensa_jugador = 100
defensa_oponente = 100

# Asiga la vida maxima a las variables de HP
PS_maximo_jugador = PS_jugador
PS_maximo_oponente = PS_oponente

# listas de tipos y multiplicadores
tipos = ["agua", "fuego", "planta"]
multiplicadores = [
    [1, 2, 0.5], # Agua contra [Agua, Fuego, Planta]
    [0.5, 1, 2], # Fuego contra [Agua, Fuego, Planta]
    [2, 0.5, 1] # Planta contra [Agua, Fuego, Planta]
]

# funcion para calcular el daño basado en la tabla de tipos usando listas
def calcular_dano(tipo_atacante,  tipo_defensor, dano_base):
    indice_atacante = tipos.index(tipo_atacante)
    indice_defensor = tipos.index(tipo_defensor)
    multiplicador = multiplicadores[indice_atacante][indice_defensor]
    return dano_base * multiplicador

while PS_jugador > 0 and PS_oponente > 0:
    ataque_jugador = input("escoja un ataque (malicioso / placaje / " + movimiento_especial + "): ")
    print("")

    # Ataques del jugador
    if ataque_jugador == "malicioso":
        defensa_oponente = defensa_oponente / 3 * 2 # Baja la defensa fisica del oponente
        print(Pokemon + " uso malicioso, el oponente redujo su defensa a " + str(round(defensa_oponente,1)))
    elif ataque_jugador == "placaje":
        dano = 35 * 100 / defensa_oponente # aumenta el impacto al bajar defensa
        PS_oponente -= dano
        if PS_oponente <= 0:
            PS_oponente = 0
        print(Pokemon + " uso placaje, el oponente recibio " + str(round(dano,1)) + " puntos de daño.")
    elif ataque_jugador == movimiento_especial:
        dano = calcular_dano(tipo_jugador, tipo_oponente, 25)
        PS_oponente -= dano
        if PS_oponente <= 0:
            PS_oponente = 0
        print(Pokemon + " uso " + movimiento_especial + ", el oponente recibio " + str(round(dano,1)) + " puntos de daño.")
    else:
        print("¿¿Que estas haciendo?? Tus ataques son malicioso, placaje y " + movimiento_especial + "!!!")
        continue  # permite al usuario intentar de nuevo

    if PS_oponente <= 0:
        break

    # Ataques del oponente
    ataque_oponente = random.randrange(0, 3)
    if ataque_oponente == 0:  # latigo
        defensa_jugador = defensa_jugador / 3 * 2
        print("El oponente uso latigo, tu defensa se redujo a " + str(round(defensa_jugador,1)))
    elif ataque_oponente == 1:  # placaje
        dano = 35 * 100 / defensa_jugador  # aumenta el impacto al bajar defensa
        PS_jugador -= dano
        if PS_jugador <= 0:
            PS_jugador = 0
        print("El oponente uso placaje, recibiste " + str(round(dano,1)) + " puntos de daño.")
    elif ataque_oponente == 2:  # movimiento especial del oponente
        dano = calcular_dano(tipo_oponente, tipo_jugador, 25)
        PS_jugador -= dano
        if PS_jugador <= 0:
            PS_jugador = 0
        print("El oponente uso " + movimiento_especial_oponente + ", recibiste " + str(round(dano,1)) + " puntos de daño.")
    else:
        print("Error en el random")

    print(Pokemon + ": " + mostrar_barra_progreso(PS_jugador, PS_maximo_jugador), str(round(PS_jugador,1)) + " PS")
    print(oponente + " oponente: " + mostrar_barra_progreso(PS_oponente, PS_maximo_oponente), str(round(PS_oponente,1)) + " PS")
    print("")


# Final del duelo Pokemon
if PS_jugador > 0:
    print(Pokemon + ": " + mostrar_barra_progreso(PS_jugador, PS_maximo_jugador), str(round(PS_jugador,1)) + " PS")
    print(oponente + " oponente: " + mostrar_barra_progreso(PS_oponente, PS_maximo_oponente), str(round(PS_oponente,1)) + " PS")
    print("")

    print(oponente + " oponente se ha debilitado.")
    print("Ganaste!")
else:
    print(Pokemon + ": " + mostrar_barra_progreso(PS_jugador, PS_maximo_jugador), str(round(PS_jugador,1)) + " PS")
    print(oponente + " oponente: " + mostrar_barra_progreso(PS_oponente, PS_maximo_oponente), str(round(PS_oponente,1)) + " PS")
    print("")

    print(Pokemon + " se ha debilitado.")
    print("Perdiste")
