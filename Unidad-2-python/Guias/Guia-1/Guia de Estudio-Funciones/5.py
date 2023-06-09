'''
Desarrollar un programa que permita al usuario ingresar una serie de numeros enteros
positivos (N numeros) hasta que ingrese -1 (Solo positivos ignorando los numeros negativos).
Luego, el programa debe calcular e imprimir en pantalla lo siguiente: el numero
mayor de los ingresados, la sumatoria total de los numeros, la sumatoria de los numeros
pares, la sumatoria de los numeros impares y el promedio total. Ademas, se debe imprimir 
si el numero mayor obtenido es mayor, menor o igual que el promedio calculado. 
Asegurate de resolver este problema utilizando las funciones que consideres adecuadas.
Nota: el -1 no se cuenta. Si el usuario ingresa un numero negativo debe volver a pedir un
numero y no se usa en el calculo. 
Ejemplo: el usuario ingresa: 2, 3, 6, 7, 7, 9, -1 se debe imprimir en pantalla:
-La suma de pares es: 8
-La suma de impares es: 26
-La suma total es: 34
-El promedio es: 5
-El numero mayor ingresado fue: 9
-El numero es mayor que el promedio y este es 9
'''

#EJERCICIO N°5
num = int(input("Ingrese los numeros que desee > "))
numeros = list()

while num < 0 :
    num = int(input("Ingrese un entero positivo > "))
else :

    print("Para cerrar el ciclo, ingrese el (-1)")

    numeros.append(num)

while num != -1 :

    if num < 0 :

        num = int(input("Ingrese un entero positivo > "))

    else :

        num = int(input("> "))
        numeros.append(num)

enteros_pos = [i for i in numeros if i >= 0]


print("Numeros ingresados exitosamente")

num_mayor = max(enteros_pos)                            #FALTA NUM MAYOR
print(f"El mayor numero ingresado es {num_mayor}")

num_suma = sum(enteros_pos)
print(f"La suma de los numeros ingresados es {num_suma}")

num_impares = [i for i in enteros_pos if (i % 2) != 0]
sum_impares= sum(num_impares)
print(f"La suma de los numeros impares ingresados es {sum_impares}")

promedio = (num_suma / len(numeros))                                    
print(f"El promedio de los numeros ingresados es {promedio}")           

if num_mayor > promedio :
    print(f"{num_mayor} es mayor que el promedio.")
else :
    print(f"{num_mayor} es menor que el promedio")