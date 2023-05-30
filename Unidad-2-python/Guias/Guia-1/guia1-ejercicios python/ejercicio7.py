'''
7. Determinar el factorial de un numero n, donde:
n! = n · (n-1) · (n-2)..,3 · 2 · 1
factorial(x) = 
|1                     si x = 0
|x · factorial(x - 1) si x ≥ 1

'''

from math import factorial

n = int(input("Ingrese su valor: "))

if n == 0 :
    print(1)
else :
    factor = n * factorial(n - 1)
    print(factor)