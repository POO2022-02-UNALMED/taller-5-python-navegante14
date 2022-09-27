from zooAnimales.animal import Animal


class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, n, e, hab, g, col, ven):
        super().__init__(n, e, hab, g)
        self.colorPiel = col
        self.venenoso = ven
        Anfibio.listado.append(self)

    def movimiento():
        return "saltar"

    @classmethod
    def cantidadAnfibios(self):
        return len(Anfibio.listado)

    @classmethod
    def crearRana(
        self,
        n,
        e,
        g,
    ):
        nuevo = Anfibio(n, e, "selva", g, "rojo", True)
        Anfibio.ranas += 1
        return nuevo

    @classmethod
    def crearSalamandra(
        self,
        n,
        e,
        g,
    ):
        nuevo = Anfibio(n, e, "selva", g, "negro y amarillo", False)
        Anfibio.salamandras += 1
        return nuevo

    def getColorPiel(self):
        return self.colorPiel

    def isVenenoso(self):
        return self.venenoso