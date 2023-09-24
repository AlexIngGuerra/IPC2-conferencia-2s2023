
class Persona:
    def __init__(self, carnet, nombre, apellido):
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido

    def toString(self):
        return self.carnet + " - "+ self.apellido + " , "+self.nombre

