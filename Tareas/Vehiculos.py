class Vehicle():
    def __init__(self, type, brand, model):
        self.type = type
        self.brand = brand
        self.model = model

    def __str__(self) -> str:
        return f"Tipo: {self.type} / Marca: {self.brand} / Modelo: {self.model}"
    
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__("Carro", brand, model)

class Ship(Vehicle):
    def __init__(self, brand, model):
        super().__init__("Barco", brand, model)

class Airplane(Vehicle):
    def __init__(self, brand, model):
        super().__init__("Avion", brand, model)
    
if __name__ == "__main__":
    # Crear dos objetos de cada tipo
    carro1 = Car('Toyota', 'Corolla')
    carro2 = Car('Ford', 'Mustang')

    barco1 = Ship('Yamaha', '242X')
    barco2 = Ship('Bayliner', 'Element E18')

    avion1 = Airplane('Boeing', '747')
    avion2 = Airplane('Airbus', 'A320')

    print(carro1, "\n", carro2, "\n", barco1, "\n", barco2, "\n", avion1, "\n", avion2)