#Programa 12 definir funciones

#defino la funcion saludar que recibe una variable string
def saludar(var_nombre):
    print("¡Buenos días, " + var_nombre + "!")

#solicito el ingreso del nombre al usuario
var_nombre = input("Ingrese su nombre: ")

#Llamo a la funcion y le paso como parametro la variable nombre
saludar(var_nombre)