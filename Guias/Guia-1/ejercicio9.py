'''
9. Se tiene la siguiente lista de enteros:
numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]
Se solicita:
a) Eliminar el ultimo elemento de la lista
b) Agregar en la primera posicion el numero 2
c) Eliminar los numeros duplicados de la lista
d) Obtener la media y la mediana de la lista

'''

import statistics

numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]
numeros.pop()
numeros.insert(0, 2)
numeros = list(set(numeros))
media = statistics.mean(numeros)
mediana = statistics.median(numeros)

print("Lista actualizada:", numeros)
print("Media:", media)
print("Mediana:", mediana)
