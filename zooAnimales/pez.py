from zooAnimales.animal import Animal


class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, n, e, hab, g, col, can):
        super().__init__(n, e, hab, g)
        self.colorEscamas = col
        self.cantidadaletas = can
        Pez.listado.append(self)

    def movimiento():
        return "nadar"

    @classmethod
    def cantidadPeces(self):
        return len(Pez.listado)

    @classmethod
    def crearSalmon(
        self,
        n,
        e,
        g,
    ):
        nuevo = Pez(n, e, "oceano", g, "rojo", 6)
        Pez.salmones += 1
        return nuevo

    @classmethod
    def crearBacalao(
        self,
        n,
        e,
        g,
    ):
        nuevo = Pez(n, e, "oceano", g, "gris", 6)
        Pez.bacalaos += 1
        return nuevo

    def getColorEscamas(self):
        return self.colorEscamas

    def getCantidadAletas(self):
        return self.cantidadaletas