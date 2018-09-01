#Programa 8: dados los catetos de un triangulo rectangulo calcular su hipotenusa
#5**(1/2) es elevar 5 por 1/2 (o 0,5)
from math import sqrt
var_cateto1 = int(input("Ingrese cateto uno: "))
var_cateto2 = int(input("Ingrese cateto dos: "))
#var_hipotenusa = ((var_cateto1 ** 2) + (var_cateto2 **2)) ** 0.5
var_hipotenusa = sqrt((var_cateto1 ** 2)+(var_cateto2 ** 2))
print("La hipotenusa es: ",var_hipotenusa)                              

