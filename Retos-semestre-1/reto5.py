'''
Hacer un algoritmo que detecte si un número es
par o impar, además si es un número primo y si es
mayor o menor a 50. Para este ejercicio se solicita
utilizar condicionales y bucles.
'''

numero= int(input("Ingrese un numero \n"))
numero_par= (numero/2 ==int)
numero_impar=(numero/2 ==float)


if numero_par:
    print("el numero es par")
elif numero_impar:
    print("el numero es impar")


