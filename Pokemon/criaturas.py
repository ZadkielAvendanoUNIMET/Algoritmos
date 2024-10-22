class pokemon:
    def __init__(self, nombre, tipo, mov1, mov2, mov3, PS, defensa):
        self.nombre = nombre
        self.tipo = tipo
        self.mov1 = mov1
        self.mov2 = mov2
        self.mov3 = mov3
        self.PS = PS
        self.defensa = defensa
    
    def obtener_datos(self):
        return (self.nombre, self.tipo, self.mov1, self.mov2, self.mov3, self.PS, self.defensa)
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Mov1: {self.mov1}, Mov2: {self.mov2}, Mov3: {self.mov3}, PS: {self.PS}, Defensa: {self.defensa}"

def crear_pokemon(nombre):
    if nombre in Pokemons:
        return pokemon(*(Pokemons[nombre]))
    else:
        print("Error critico")
        quit()

Pokemons = {
    "Oshawoot" : ("Oshawoot", "agua", "placaje", "hidro pulso", "malicioso", 150, 100),
    "Cyndaquil" : ("Cyndaquil", "fuego", "placaje", "ascuas", "malicioso", 150, 100),
    "Rowlet" : ("Rowlet", "planta", "placaje", "hoja afilada", "malicioso", 150, 100)
}
