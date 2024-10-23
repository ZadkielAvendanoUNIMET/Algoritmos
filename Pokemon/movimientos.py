# Nombre del movimiento, Tipo del movimiento ( fisico, especial, estado)
    # Ataques fisicos y especiales: Tipo del ataque, Daño del ataque
    # Movimientos de estado:  Tipo de estado, Atributo a cambiar, Operaciones a cambiar, False/Oponente o True/Usuario
movimiento = {
    # Ataques Fisicos
    "placaje": {"clase": "fisico", "tipo": "normal", "potencia": 40},

    # Ataques Especiales
    "ascuas": {"clase": "especial", "tipo": "fuego", "potencia": 40},
    "burbuja": {"clase": "especial", "tipo": "agua", "potencia": 40},
    "latigo cepa": {"clase": "especial", "tipo": "planta", "potencia": 40},
    "impactrueno": {"clase": "especial", "tipo": "electrico", "potencia": 25},

    # Movimientos de Estado
    "malicioso": {"clase": "estado", "tipo": "normal", "atributo": "Def", "efecto": 2/3, "usuario": False},
    "gruñido": {"clase": "estado", "tipo": "normal", "atributo": "Atk", "efecto": 2/3, "usuario": False},
    "refugio": {"clase": "estado", "tipo": "agua", "atributo": "Def", "efecto": 4/3, "usuario": True}
}