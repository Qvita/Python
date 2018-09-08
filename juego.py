#nombre, salud, poder, defensa
#("Pocho", 100,50,90)
 personaje1= {"nombre":"Qvita", "salud":100, "poder":70, "defensa":70}
# keys nombre salud poder defensa el resto son valroes
print(personaje1["nombre"])
print(personaje1["salud"])
print(personaje1["poder"])
print(personaje1["defensa"])
#esto es un diccionario, son mutables al igual que las listas
personaje1["poder"]=90
print(personaje1.get("vuelo", "no vuela"))
#valores=("hola",[10,20,(30,4), 25)
#valores [1][2][1] el 2 me va a devolver el 30,4, y el uno final me devuelve el 4
#[10,20,(30,4)]