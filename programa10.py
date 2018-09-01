#Programa 10. Condiciones.
var_edad = int(input("Ingrese edad: "))

if(var_edad >= 15 and var_edad <= 20):
    print("Mensaje de 15 a 20")
elif(var_edad >= 25 and var_edad <= 30):
    print("Mensaje de 25 a 30")
elif(var_edad >= 35 and var_edad <= 40):
    print("Mensaje de 35 a 40")
else:
    if(var_edad < 15):
        print("Es menor de edad")
    else:
        print("Es más viejo")