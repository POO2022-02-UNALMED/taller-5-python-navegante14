from zooAnimales.animal import Animal


class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, n, e, hab, g, col):
        super().__init__(n, e, hab, g)
        self.colorPlumas = col
        Ave.listado.append(self)

    def movimiento():
        return "volar"

    @classmethod
    def cantidadAves(self):
        return len(Ave.listado)

    @classmethod
    def crearHalcon(
        self,
        n,
        e,
        g,
    ):
        nuevo = Ave(n, e, "monatanas", g, "cafe glorioso")
        Ave.halcones += 1
        return nuevo

    @classmethod
    def crearAguila(
        self,
        n,
        e,
        g,
    ):
        nuevo = Ave(n, e, "montanas", g, "blanco y amarillo")
        Ave.aguilas += 1
        return nuevo

    def getColorPlumas(self):
        return self.colorPlumas