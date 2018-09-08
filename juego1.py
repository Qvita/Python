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

    p1=crear_personaje(nombre="Qvita", ataque = 170, salud = 2000)
    p2=crear_personaje(nombre="Xote", ataque = 2 , salud = 2)
    print(p2)
    atacar(p1,p2)
    print(p2)
    if(p2["salud"] < 0 ):
        print(p2["nombre"],  "cago fuego")

if __name__=="__main__":
    probar()


