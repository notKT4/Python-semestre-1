'''
4. Desarrollar un algoritmo que permita devolver la siguiente propiedad descubierta por
Nicomaco de Gerasa: 
Sumando el primer impar, se obtiene el primer cubo.
Sumando los dos siguientes impares, se obtiene el segundo cubo
Sumando los tres siguientes, se obtiene el tercer cubo, y asi sucesivamente.
Ejemplo:
1**3 = 1 = 1
2**3 = 3 + 5 = 8
3**3 = 7 + 9 + 11 = 27
4**3 = 13 + 15 + 17 + 19 = 64
Imprimir por pantalla, los primeros n cubos, considerando el valor de n obtenido desde
teclado.
'''

n = int(input("Ingrese el valor que sera elevado al cubo: "))

f = (n * (n - 1)) + 1

if (n / 2) == float :
    r = (n ** 2) + (n + 1)
else :
    r = (n ** 2) + n

nicomaco = list(range(f, r, 2)) 

cubo = sum(nicomaco)

print("El resultado de elevar ", n,"al cubo es: ",cubo)