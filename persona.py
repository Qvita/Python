
class Persona:
    nombre = None
    apellido = None
    edad = None
    vida = None
    velocidad = None
    fuerza = None

    def __init__ (self, nombre, apellido, edad, vida, velocidad, fuerza):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.vida = vida
        self.velocidad = velocidad
        self.fuerza = fuerza

    def saludar(self):
        plantilla = "Hola, mi nombre es {nombre} {apellido}, "
        plantilla += "mi edad es {edad}."
        saludo = plantilla.format(
            nombre = self.nombre,
            apellido = self.apellido,
            edad = self.edad
        ) 
        return saludo