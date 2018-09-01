def Var_Farenheit(grados):
    #grados = int(input("Definir Temperatura Farenheit "))
    total = grados - 32
    total = (total*5)/9
    return total

#programa 14. Ejercicio 3.1 de la guia

def convertir_a_segundos(hs, mins, segs):
    total = segs
    total += mins * 60
    total += hs * 3600
    return total

def segundosahms (segs):
    horas = int(segs/3600)
    minutos = int((segs-horas*3600)/60)
    segundos = segs-(horas*3600+minutos*60)
    return horas, minutos, segundos

