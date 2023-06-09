'''
Realizar un programa donde el usuario indique la cantidad de numeros que va a ingresar,
luego solicitar dicha cantidad de numeros e imprimir en pantalla, la suma de todos 
estos numeros, la suma de los pares y la suma de los impares. Se debe resolver utilizando
funciones para cada una de las operaciones mencionadas anteriormente.

'''
#EJERCICIO N°1
def ingresar_numeros():
    ingresar = int(input("Escriba la cantidad de números que va a ingresar: "))
    lista = []

    for i in range(ingresar):
        numero = int(input("> "))
        lista.append(numero)

    return lista


def sum_numeros(lista):
    sumatoria = sum(lista)

    return sumatoria


def pares_impares(lista):
    par = []
    impar = []

    for i in range(len(lista)):
        if i % 2 == 0:
            par.append(lista[i])
        else:
            impar.append(lista[i])

    return par, impar


lista = ingresar_numeros()
print("Los números ingresados son:", lista)

sum_total = sum_numeros(lista)
print("La sumatoria de los números ingresados es:", sum_total)

par, impar = pares_impares(lista)
sum_pares = sum_numeros(par)
sum_impares = sum_numeros(impar)

print("La sumatoria de los números pares ingresados es:", sum_pares)
print("La sumatoria de los números impares ingresados es:", sum_impares)