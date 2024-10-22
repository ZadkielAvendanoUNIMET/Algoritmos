import multiplicadores
import movimientos

# funcion para calcular el daño basado en la tabla de tipos
def calcular_dano(tipo_atacante,  tipo_defensor, dano_base):
    multiplicador = multiplicadores.multiplicador_dano(tipo_atacante, tipo_defensor)
    return dano_base * multiplicador

# funcion para efectuar un movimiento
def movimiento(mov, def_mov, Ps, tipo_oponente):
    if mov in movimientos.movimiento:
        tupla = movimientos.movimiento[mov]
        indice_mov = tupla[0]
        tipo_mov = tupla[1]
        if indice_mov == 1 or indice_mov == 2: # Ataque
            dano_mov = tupla[2]
            dano_mov = calcular_dano(tipo_mov, tipo_oponente, dano_mov)
            if indice_mov == 2: # Ataque Especial
                Ps -= dano_mov
            else: # Ataque Fisico
                Ps -= dano_mov * 100 / def_mov
        elif indice_mov == 3: # Movimiento de estado
            att_mov = tupla[2]
            if att_mov == "Def":
                def_mov = def_mov * tupla[3]
            else:
                print("\n Se produjo un error al intentar efectuar el movimiento.")
                quit()
        else:
            print("\n Se produjo un error al intentar efectuar el movimiento.")
            quit()
    else:
        print("\n Se produjo un error al intentar efectuar el movimiento.")
        quit()
    
    return Ps, def_mov