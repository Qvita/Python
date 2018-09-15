var_n1 = input("Inserte nombre del Jugador 1 ")
var_n2 = input("Inserte nombre del jugador 2 ")

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

    p1=crear_personaje(nombre=var_n2, ataque = 170, salud = 2000)
    p2=crear_personaje(nombre=var_n1, ataque = 2 , salud = 2)
    print("Oh no!", var_n2 , " se la dio a" , var_n1)
    print(p2)
    atacar(p1,p2)
    print(p2)
    if(p2["salud"] < 0 ):
        print(p2["nombre"],  "cago fuego")

if __name__=="__main__":
    probar()

