class Animal:
    totalAnimales=0
    mamifero=0
    ave=0
    pez=0
    reptil=0
    anfibio=0
    def __init__(self,nombre,edad,habitat,genero):
        self.nombre=nombre
        self.edad=edad
        self.habitat=habitat
        self.genero=genero
        self.zona=None
        self.totalAnimales+=1
    def toString(self):
        if self.zona!=None:
            return "Mi nombre es "+self.nombre+", tengo una edad de "+str(self.edad)+", habito en "+self.habitat+" y mi genero es "+self.genero+", la zona en la que me ubico es "+self.zona.getNombre+", en el "+self.zona.getZoo
        else:
            return "Mi nombre es "+self.nombre+", tengo una edad de "+str(self.edad)+", habito en "+self.habitat+" y mi genero es "+self.genero
    @classmethod
    def totalPorTipo(cls):
        return "Mamiferos : "+str(cls.mamifero)+"\nAves : "+str(cls.ave)+"\nReptiles : "+str(cls.reptil)+"\nPeces : "+str(cls.pez)+"\nAnfibios : "+str(cls.anfibio)
    def movimiento(self):
        return "desplazarse"
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getGenero(self):
        return self.genero
    def getHabitat(self):
        return self.habitat