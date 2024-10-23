import multiplicadores
import movimientos
import criaturas

# funcion para calcular el daño basado en la tabla de tipos
def calcular_dano(tipo_atacante,  tipo_defensor, dano_base):
    multiplicador = multiplicadores.multiplicador_dano(tipo_atacante, tipo_defensor)
    efectividad = ""
    if multiplicador == 2:
        efectividad = "Es muy efectivo"
    elif multiplicador == 0.5:
        efectividad = "Es poco efectivo"
    elif multiplicador == 0:
        efectividad = "No tiene efecto"

    return dano_base * multiplicador, efectividad

# funcion para efectuar un movimiento
def movimiento(movimiento: str, atacante: criaturas.pokemon, defensor: criaturas.pokemon):
    try:
        if movimiento in movimientos.movimiento:
            mov = movimientos.movimiento[movimiento]
            clase_mov = mov["clase"]
            tipo_mov = mov["tipo"]
            defensor_ps = defensor.PS

            if clase_mov == "fisico" or clase_mov == "especial":  # Ataque
                potencia_mov = mov["potencia"]
                potencia_mov, efectividad = calcular_dano(tipo_mov, defensor.tipo, potencia_mov)
                if clase_mov == "especial":  # Ataque Especial
                    defensor.PS -= (potencia_mov * (atacante.ataque_especial / defensor.defensa_especial))
                else:  # Ataque Fisico
                    defensor.PS -= (potencia_mov * (atacante.ataque / defensor.defensa))
                msg = f"{defensor.nombre} recibio {str(round((defensor_ps-defensor.PS),1))} puntos de daño. {efectividad}"

            elif clase_mov == "estado":  # Movimiento de estado
                if mov["atributo"] == "Def":
                    if mov["usuario"]:
                        atacante.defensa = atacante.defensa * mov["efecto"]
                        afectado = atacante.nombre
                    else:
                        defensor.defensa = defensor.defensa * mov["efecto"]
                        afectado = defensor.nombre
                        
                    if mov["efecto"] > 1:
                        msg = f"La defensa de {afectado} subio"
                    else:
                        msg = f"La defensa de {afectado} bajo"

                elif mov["atributo"] == "Atk":
                    if mov["usuario"]:
                        atacante.ataque = atacante.ataque * mov["efecto"]
                        afectado = atacante.nombre
                    else:
                        defensor.ataque = defensor.ataque * mov["efecto"]
                        afectado = defensor.nombre
                        
                    if mov["efecto"] > 1:
                        msg = f"El ataque de {afectado} subio"
                    else:
                        msg = f"El ataque de {afectado} bajo"
                        
                else:
                    raise ValueError("Movimiento de estado no válido")
            else:
                raise ValueError("Indice de movimiento no válido")
        else:
            raise ValueError("Movimiento no encontrado")
    except ValueError as error:
        print("\nSe produjo un error al intentar efectuar el movimiento:", error)
        quit()

    return msg
