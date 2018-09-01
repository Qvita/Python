from funciones import segundosahms
from funciones import convertir_a_segundos

hs1 = int(input("Ingrese hs 1: "))
min1 = int(input("Ingrese min 1: "))
segs1 = int(input("Ingrese segs 1: "))

hs2 = int(input("Ingrese hs 2: "))
min2 = int(input("Ingrese min 2: "))
segs2 = int(input("Ingrese segs 2: "))

segundos1 = convertir_a_segundos(hs1, min1, segs1)
segundos2 = convertir_a_segundos(hs2, min2, segs2)

Ver_segundos = (segundos1 + segundos2)

print ("Ambos totales son", segundos1 ,"y", segundos2,", y la suma nos da como resultado ", Ver_segundos, "Y puto el que lee", segundosahms(Ver_segundos))