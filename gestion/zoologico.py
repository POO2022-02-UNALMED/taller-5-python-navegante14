class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregarZonas(self, z):
        self.zonas.append(z)

    def cantidadTotalAnimales(self):
        l=[]
        for i in self.zonas:
            l.append(i.cantidadAnimales())
        return sum(l)

    def getNombre(self):
        return self.nombre

    def getUbicacion(self):
        return self.ubicacion

    def getZona(self):
        return self.zonas


class Zona:
    def __init__(self, nombre, zoo=None) -> None:
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def agregarAnimales(self, a):
        self.animales.append(a)

    def cantidadAnimales(self):
        return len(self.animales)

    def getNombre(self):
        return self.nombre

    def getAnimales(self):
        return self.animales

    def getZoo(self):
        return self.zoo