'''
Construir un algoritmo que permita generar enteros de 3 en 3 comenzado por el 2 hasta el
valor máximo que será menor que 30. Calcular la suma de los enteros generados que sean
divisibles por 5, y la suma de los enteros generados que sean impares.
'''
numero=2
divisibles=0
impares=0
while numero<30:
    numero+=3
    print(numero)
    if numero%2 !=0:
        divisibles+=numero
    if numero%5 ==0:
        impares+=numero
print(impares,divisibles)


