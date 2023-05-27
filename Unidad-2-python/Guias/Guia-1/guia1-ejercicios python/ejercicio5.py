'''
5. Crear 20 numeros, que se encuentren en el intervarlo 40 al 350 y los almacene en una
lista y luego pida buscar algun numero dentro de los almacenados. Ademas que muestre
la cantidad de ocurrencias de ese numero buscado. (Se permite el uso de la Biblioteca
Random)
'''
#ALGORITMO OCURRENCIAS

import random
n=random.sample(range(40,350),20)

print(n)
print(" ")

nSEARCH=int(input("Que numero desea buscar?\n"))

ocurrN= n.count(nSEARCH)

print(f"El numero {nSEARCH} tiene {ocurrN} numero de ocurrencias")