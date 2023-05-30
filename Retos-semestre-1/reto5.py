'''
Hacer un algoritmo que detecte si un número es
par o impar, además si es un número primo y si es
mayor o menor a 50. Para este ejercicio se solicita
utilizar condicionales y bucles.
'''

numero= int(input("Ingrese un numero \n"))

if numero > 50:
    print("El numero es mayor a 50")
elif numero == 50:
    print("El numero es 50")
else:
    print("El numero es menor a 50")

def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

if primo:
    print("El numero es primo")

if numero % 2 ==0:
    print("El numero es par")

if numero % 2 !=0:
    print("El numero es impar")


