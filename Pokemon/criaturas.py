class pokemon:
    def __init__(self, Nombre, Tipo, Movimiento_1, Movimiento_2, Movimiento_3, PS, Ataque, Defensa, Ataque_Especial, Defensa_Especial, Velocidad):
        self.nombre = Nombre
        self.tipo = Tipo
        self.mov1 = Movimiento_1
        self.mov2 = Movimiento_2
        self.mov3 = Movimiento_3
        self.PS = PS
        self.ataque = Ataque
        self.defensa = Defensa
        self.ataque_especial = Ataque_Especial
        self.defensa_especial = Defensa_Especial
        self.velocidad = Velocidad
        
    def obtener_datos(self):
        return (
            self.nombre,
            self.tipo,
            self.mov1,
            self.mov2,
            self.mov3,
            self.PS,
            self.ataque,
            self.defensa,
            self.ataque_especial,
            self.defensa_especial,
            self.velocidad
        )
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Mov1: {self.mov1}, Mov2: {self.mov2}, Mov3: {self.mov3}, PS: {self.PS}, Ataque: {self.ataque}, Defensa: {self.defensa}, Ataque Especial: {self.ataque_especial}, Defensa Especial: {self.defensa_especial}, Velocidad: {self.velocidad}"

def crear_pokemon(nombre):
    if nombre in Pokemons:
        datos = Pokemons[nombre]
        return pokemon(**datos)
    else:
        print("Error crítico")
        quit()

Pokemons = {
    "Oshawott": {
        "Nombre": "Oshawott",
        "Tipo": "agua",
        "Movimiento_1": "placaje",
        "Movimiento_2": "burbuja",
        "Movimiento_3": "refugio",
        "PS": 352,
        "Ataque": 218,
        "Defensa": 209,
        "Ataque_Especial": 208,
        "Defensa_Especial": 191,
        "Velocidad": 202
    },
    "Cyndaquil": {
        "Nombre": "Cyndaquil",
        "Tipo": "fuego",
        "Movimiento_1": "placaje",
        "Movimiento_2": "ascuas",
        "Movimiento_3": "gruñido",
        "PS": 304,
        "Ataque": 224,
        "Defensa": 188,
        "Ataque_Especial": 264,
        "Defensa_Especial": 203,
        "Velocidad": 254
    },
    "Rowlet": {
        "Nombre": "Rowlet",
        "Tipo": "planta",
        "Movimiento_1": "placaje",
        "Movimiento_2": "latigo cepa",
        "Movimiento_3": "malicioso",
        "PS": 332,
        "Ataque": 245,
        "Defensa": 227,
        "Ataque_Especial": 177,
        "Defensa_Especial": 227,
        "Velocidad": 181
    },
    "Pikachu": {
        "Nombre": "Pikachu",
        "Tipo": "electrico",
        "Movimiento_1": "placaje",
        "Movimiento_2": "impactrueno",
        "Movimiento_3": "malicioso",
        "PS": 274,
        "Ataque": 229,
        "Defensa": 154,
        "Ataque_Especial": 218,
        "Defensa_Especial": 179,
        "Velocidad": 306
    }
}
