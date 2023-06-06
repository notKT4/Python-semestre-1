'''
Crear un algoritmo que permita saber si un año es bisiesto (calendario gregoriano) 
desde el año 0 en adelante. Utilizar funciones para resolver el problema. 

'''
def bisiesto(año):
    if año%4==0:
        return False
    else:
        return True

año=int(input("Año >> "))

if bisiesto(año):
    print(f"{año} es bisiesto")
else:
    print(f"{año} es no bisiesto")
