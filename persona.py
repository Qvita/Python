
class Persona:
    nombre = None
    edad = None
    vida = None
    velocidad = None
    fuerza = None

    def __init__ (self, nombre, edad, vida, velocidad, fuerza):
        self.nombre = nombre
        self.edad = edad
        self.vida = vida
        self.velocidad = velocidad
        self.fuerza = fuerza

    def saludar(self):
        plantilla = "\n Bienvenido {nombre}, yo soy la interfaz"
        plantilla += "\n Tus características son \n Vida {vida} \n Velocidad {velocidad} \n Fuerza {fuerza}. \n"
        saludo = plantilla.format(
            nombre = self.nombre,
            edad = self.edad,
            vida = self.vida,
            velocidad = self.velocidad,
            fuerza = self.fuerza
        ) 
        return saludo