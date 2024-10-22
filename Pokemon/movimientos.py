# Nombre del movimiento, Tipo del movimiento (1: Ataque fisico, 2: Ataque especial, 3: Movimiento de estado)
    # Ataques fisicos y especiales: Tipo del ataque, Daño del ataque
    # Movimientos de estado:  Tipo de estado, Atributo a cambiar, False/Disminuye o True/Sube, Operaciones a cambiar
movimiento = {
    # Ataques Fisicos
    "placaje": (1, "normal", 35),

    # Ataques Especiales
    "ascuas": (2, "fuego", 25),
    "hidro pulso": (2, "agua", 25),
    "hoja afilada": (2, "planta", 25),

    # Movimientos de Estado
    "malicioso": (3, "normal", "Def", 2/3)
}