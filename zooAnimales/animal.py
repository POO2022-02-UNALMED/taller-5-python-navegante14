class Animal:
    totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero) -> None:
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero

    def movimiento():
        return "desplazarse"

    @classmethod
    def totalPorTipo(self):

        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        from zooAnimales.anfibio import Anfibio

        stri = (
            "Mamiferos : "
            + str(Mamifero.cantidadMamiferos())
            + "\nAves : "
            + str(Ave.cantidadAves())
            + "\nReptiles : "
            + str(Reptil.cantidadReptiles())
            + "\nPeces : "
            + str(Pez.cantidadPeces())
            + "\nAnfibios : "
            + str(Anfibio.cantidadAnfibios())
        )
        return stri

    def toString(self) -> str:
        stri = "Mi nombre es",self.nombre,"tengo una edad de",self.edad,"habito en",self.habitat,"y mi genero es",self.genero
        
        return stri

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getHabitat(self):
        return self.habitat

    def getGenero(self):
        return self.genero