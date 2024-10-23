def multiplicador_dano(tipo_jugador, tipo_oponente):
    # Matriz de efectividad de tipos
    efectividad = {
        'fuego': {'fuego': 0.5, 'planta': 2.0, 'agua': 0.5, 'normal': 1.0, 'lucha': 1.0, 'volador': 1.0, 'tierra': 1.0, 'roca': 0.5, 'electrico': 1.0},
        'planta': {'fuego': 0.5, 'planta': 0.5, 'agua': 2.0, 'normal': 1.0, 'lucha': 1.0, 'volador': 0.5, 'tierra': 2.0, 'roca': 2.0, 'electrico': 1.0},
        'agua': {'fuego': 2.0, 'planta': 0.5, 'agua': 0.5, 'normal': 1.0, 'lucha': 1.0, 'volador': 1.0, 'tierra': 2.0, 'roca': 2.0, 'electrico': 1.0},
        'normal': {'fuego': 1.0, 'planta': 1.0, 'agua': 1.0, 'normal': 1.0, 'lucha': 1.0, 'volador': 1.0, 'tierra': 1.0, 'roca': 0.5, 'electrico': 1.0},
        'lucha': {'fuego': 1.0, 'planta': 1.0, 'agua': 1.0, 'normal': 2.0, 'lucha': 1.0, 'volador': 0.5, 'tierra': 1.0, 'roca': 2.0, 'electrico': 1.0},
        'volador': {'fuego': 1.0, 'planta': 2.0, 'agua': 1.0, 'normal': 1.0, 'lucha': 2.0, 'volador': 1.0, 'tierra': 1.0, 'roca': 0.5, 'electrico': 0.5},
        'tierra': {'fuego': 2.0, 'planta': 0.5, 'agua': 1.0, 'normal': 1.0, 'lucha': 1.0, 'volador': 0.0, 'tierra': 1.0, 'roca': 2.0, 'electrico': 2.0},
        'roca': {'fuego': 2.0, 'planta': 1.0, 'agua': 1.0, 'normal': 1.0, 'lucha': 0.5, 'volador': 2.0, 'tierra': 0.5, 'roca': 1.0, 'electrico': 1.0},
        'electrico': {'fuego': 1.0, 'planta': 0.5, 'agua': 2.0, 'normal': 1.0, 'lucha': 1.0, 'volador': 2.0, 'tierra': 0.0, 'roca': 1.0, 'electrico': 0.5}
    }

    if tipo_jugador not in efectividad or tipo_oponente not in efectividad[tipo_jugador]:
        raise ValueError("Tipo de Pokémon no válido")

    # Obtener el multiplicador de daño
    return efectividad[tipo_jugador][tipo_oponente]
