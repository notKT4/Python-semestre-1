'''
2. Construir un programa permita calcular e imprimir el resultado de la siguiente sumatoria:
S = 500 + 456 + 510 + 454 + 520 + 452 + ... + 800 
'''

X = 500
Y = 456

lista_X = list()
lista_Y = list()

while X < 800 :
    X += 10
    Y -= 2

    print(X)
    print(Y)
    lista_X.append(X)
    lista_Y.append(Y)

suma_X = sum(lista_X)
suma_Y = sum(lista_Y)

S = sum((suma_X, suma_Y))

print(S)