from persona import Persona
#from juego1 import *

var_nombre = input("\n Nombre? ")
var_apellido = input("Apellido? ")
var_edad = input("Edad?" )

print("\n Por favor ingrese valores a las siguientes habilidades. Vida, Velocidad y fuerza. Recuerde que entre las 3 no puede sumar más de 20")

var_error = 0

while (var_error == 0):
    var_vida = int(input("\n Vida? "))
    if var_vida < 21:
        var_error = 1
    else:
        print("\n Abajo de 20 crack")

print("\n Quedan " , 20-var_vida , "puntos disponibles \n ")

var_error = 2
while (var_error == 2):
    var_velocidad = int(input("\n Velocidad? "))
    if var_vida+var_velocidad < 21:
        var_error = 3
    else:
        print("\n Abajo de 20 Total")

print("\n Quedan " , 20-var_vida-var_velocidad , "puntos disponibles")

var_error = 4
while (var_error == 4):
    var_fuerza = int(input("\n Fuerza? "))
    if var_vida+var_velocidad+ var_fuerza < 21:
        var_error = 5
    else:
        print("\n Bue...")

   
p1 = Persona (var_nombre, var_apellido, var_edad, var_vida, var_velocidad, var_fuerza)
print(p1.saludar())