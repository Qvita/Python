#Programa 13 retornar un valor desde una funcion.abs

#defino la funcion saludar que recibe un nombre y devuelve una concatenacion
# el valor nuevo se almacena en var_nombre
def saludar(var_nombre):
    return "¡Buenos días, " + var_nombre + "!"

#solicito el ingreso de un nombre al usuario
var_nombre = input("Ingrese su nombre: ")

#recibo el resultado de la concatenacion
var_saludo = saludar(var_nombre)  

#imprimo la variable saludo en la que se almaceno lo que devolvio la funcion con el parametro nombre
print(var_saludo)