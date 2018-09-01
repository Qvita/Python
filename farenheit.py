def Var_Farenheit(grados):
    #grados = int(input("Definir Temperatura Farenheit "))
    total = grados - 32
    total = (total*5)/9
    return total

#print("La temperatura en grados centigrados es de " + str(total))
grados = int(input("Definir Temperatura Farenheit "))
print(Var_Farenheit(grados))
for i in range(0,130,10):
    print((i) , Var_Farenheit (i))
