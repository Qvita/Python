from persona import Persona
#from combate import *

var_nombre = input("\n Apodo? ")
var_edad = input(" Edad? " )

var_n1 = input (" Nombre del rival? ")
var_edad2 = input (" Y tu edad muchachito? ")

print("\n Por favor ingrese valores a las siguientes habilidades. \n Vida, Velocidad y fuerza. Recuerde que entre las 3 no puede sumar más de 20")

var_error = 0

while (var_error == 0):
    var_vida = int(input("\n Vida? "))
    if var_vida < 21:
        var_error = 1
    else:
        print("\n Abajo de 20 crack")

print("Quedan " , 20-var_vida , "puntos disponibles ")

var_error = 2
while (var_error == 2):
    var_velocidad = int(input("Velocidad? "))
    if var_vida+var_velocidad < 21:
        var_error = 3
    else:
        print("\n Abajo de 20 pero en total \n Quedan " , 20-var_vida , "puntos disponibles \n ")

print("Quedan " , 20-var_vida-var_velocidad , "puntos disponibles")

var_error = 4
while (var_error == 4):
    var_fuerza = int(input("Fuerza? \n"))
    if var_vida+var_velocidad+ var_fuerza < 21:
        var_error = 5
    else:
        print("\n Bue... va de nuevo \n Quedan " , 20-var_vida-var_velocidad , "puntos disponibles")

var_clase = int(input("\n Ahora elije una clase, selecciona con 1, 2 o 3. \n 1. Peronista \n 2. Radical \n 3. Ultra Derecha \n "))

if (var_clase == 1):
    var_vida = var_vida + 10
    print("\nEres Peronista, como van a durar para siempre obtienes 10 puntos extra de vida")
elif (var_clase == 2):
    var_velocidad = var_velocidad + 10
    print("\nTienes la velocidad de un radical para hacer alianza con cualquiera \n Sumaste 10 puntos de velocidad")
elif (var_clase == 3 ):
    var_fuerza = var_fuerza + 10
    print("\nElejiste Ultra derecha y obtienes +10 en fuerza bruta como es lógico")
else:
        print("Las opciones son 1, 2 o 3. \n")

print("\n Muy bien, ahora vamos a seguir con las características y clases de" , var_n1 , "que siendo sincero me cae un poco mejor")



var_error = 0

while (var_error == 0):
    var_vida2 = int(input("\n Vida? "))
    if var_vida2 < 21:
        var_error = 1
    else:
        print("\n Dale, ya lo expliqué. Abajo de 20.")

print("Quedan " , 20-var_vida2 , "puntos disponibles ")

var_error = 2
while (var_error == 2):
    var_velocidad2 = int(input("Velocidad? "))
    if var_vida2+var_velocidad2 < 21:
        var_error = 3
    else:
        print("\n No lo voy a explicar de nuevo \n Quedan " , 20-var_vida2 , "puntos disponibles \n ")

print("Quedan " , 20-var_vida2-var_velocidad2 , "puntos disponibles")

var_error = 4
while (var_error == 4):
    var_fuerza2 = int(input("Fuerza? \n"))
    if var_vida2+var_velocidad2+ var_fuerza2 < 21:
        var_error = 5
    else:
        print("\n Porque no kiteas y listo? \n Quedan " , 20-var_vida2-var_velocidad2 , "puntos disponibles")

var_clase = int(input("Ahora elije una clase, selecciona con 1, 2 o 3. \n 1. Peronista \n 2. Radical \n 3. Ultra Derecha \n "))

if (var_clase == 1):
    var_vida2 = var_vida2 + 10
    print("\nEres Peronista, como van a durar para siempre obtienes 10 puntos extra de vida")
elif (var_clase == 2):
    var_velocidad2 = var_velocidad2 + 10
    print("\nTienes la velocidad de un radical para hacer alianza con cualquiera \n Sumaste 10 puntos de velocidad")
elif (var_clase == 3 ):
    var_fuerza2 = var_fuerza2 + 10
    print("\nElejiste Ultra derecha y obtienes +10 en fuerza bruta como es lógico")
else:
        print("Las opciones son 1, 2 o 3. \n")



#
p1 = Persona (var_nombre, var_edad, var_vida, var_velocidad, var_fuerza )
print(p1.saludar())

p2 = Persona (var_n1, var_edad2, var_vida2, var_velocidad2, var_fuerza2 )
print(p2.saludar())

def crear_personaje(nombre = "Jugador", ataque = 10, salud = 10):
#esto construye un diccionario y lo retorna
    personaje={
        "nombre": nombre,
        "ataque": ataque,
        "salud": salud
    }
    return personaje
def atacar(atacante, atacado):

    #atacado["salud"]-=atacante["poder"]
    recibir_ataque (atacado, atacante["ataque"])

def recibir_ataque (personaje, ataque):
    personaje["salud"]-= ataque 
def probar():

    p1=crear_personaje(nombre = var_nombre, ataque = var_fuerza, salud = var_vida)
    p2=crear_personaje(nombre = var_n1, ataque = var_fuerza2 , salud = var_vida2)
    print("Oh no!", var_nombre , " se la agito a" , var_n1)
    print(p2)
    atacar(p1,p2)
    print(var_n1 , "Quedó medio juguete \n" , p2)
    if(p2["salud"] < 0 ):
        print(p2["nombre"],  "cago fuego")
    else:
        print("Y ahora que de que te disfrazas?\n" ,p1)
    atacar(p2,p1)
    if (p1["salud"] < 0 ):
        print (p1["nombre"],  "La quedo")
    else: 
        print("Que pelea aburrida, no la queda ninguno \n Acá podría hacer un loop hasta que muera alguno, pero voy a intentar que puedan seleccionar ataques. \n Y los modificadores de velocidad y edad todavía no los estoy usando")

if __name__=="__main__":
    probar()