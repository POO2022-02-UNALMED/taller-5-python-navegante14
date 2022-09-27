from zooAnimales.animal import Animal


class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, n, e, hab, g, pel, pat):
        super().__init__(n, e, hab, g)
        self.pelaje = pel
        self.patas = pat
        Mamifero.listado.append(self)

    @classmethod
    def cantidadMamiferos(self):
        return len(Mamifero.listado)

    @classmethod
    def crearCaballo(
        self,
        n,
        e,
        g,
    ):
        nuevo = Mamifero(n, e, "pradera", g, True, 4)
        Mamifero.caballos += 1
        return nuevo

    @classmethod
    def crearLeon(
        self,
        n,
        e,
        g,
    ):
        nuevo = Mamifero(n, e, "selva", g, True, 4)
        Mamifero.leones += 1
        return nuevo

    def isPelaje(self):
        return self.pelaje

    def getPatas(self):
        return self.patas