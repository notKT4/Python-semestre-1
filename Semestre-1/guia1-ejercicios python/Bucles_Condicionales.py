#Ejercicios resueltos de la guia "Bucles Y Condicionales"
#Integrantes : Simon Perez, Felipe Pino y Vicente Salazar

#EJERCICIO N°1
texto= """La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional 
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus 
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion
democratica""" 

quitar=",.;:\n!\""
for caracter in quitar:           #quitamos los puntos y comas 
    texto=texto.replace(caracter,
                    "")   
texto=texto.lower()               #combierte las letras mayusculas a minusculas       
v1=texto.count("universidad")
palabras=texto.split()
tupla1=tuple(palabras)     

print("la palabra universidad se repite",v1,"veces") 
#print(tupla2)    
print(tupla1) 
print(type(tupla1)) 

#En la guia no espesificaba si la tupla tenia que tener todas las palabras o solo las 3 veces que se 
#repite universidad, asi que hice que la tupla tubiera todas las palabras del texto .


#EJERCICIO N°2
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


#EJERCICIO N°3
Tdiurno = 12000
Tnocturno = 16000

domD= Tdiurno+2000
domN= Tnocturno+3000

print("Pago diario empleado 1")
emp1={
    "Lunes":Tnocturno*10,
    "Martes":Tnocturno*10,
    "Miercoles":Tnocturno*10,
    "Jueves":Tdiurno*10,
    "Viernes":Tdiurno*10,
}
print(emp1)
print(" ")

print("Pago diario empleado 2")
emp2={
    "Martes":Tnocturno*10,
    "Miercoles":Tnocturno*10,
    "Jueves":Tdiurno*10,
    "Domingo":domD*10,
}
print(emp2)
print(" ")

print("Pago diario empleado 3")
emp3={
    "Sabado":Tnocturno*10,
    "Domingo":domN*10,
    "Miercoles":Tnocturno*10,
    "Jueves":Tdiurno*10,
    "Viernes":Tdiurno*10,
}
print(emp3)
print(" ")

tsemanal1=sum(emp1.values())
tsemanal2=sum(emp2.values())
tsemanal3=sum(emp3.values())

tsemanal={
    'Empleado 1':tsemanal1,
    'Empleado 2':tsemanal2,
    'Empleado 3':tsemanal3,
}

print("Ls tarifas semanales son: \n")
print(tsemanal)
print(" ")


#EJERCICIO N°4
n = int(input("Ingrese el valor que sera elevado al cubo: "))

f = (n * (n - 1)) + 1

if (n / 2) == float :
    r = (n ** 2) + (n + 1)
else :
    r = (n ** 2) + n

nicomaco = list(range(f, r, 2)) 

cubo = sum(nicomaco)

print("El resultado de elevar ", n,"al cubo es: ",cubo)

""""

1 ** 3 = 1
2 ** 3 = 3 + 5
3 ** 3 = 7 + 9 + 11
4 ** 3 = 13 + 15 + 17 + 19
5 ** 3 = 21 + 23 + 25 + 27 + 29

"""

#EJERCICIO N°5
import random
n=random.sample(range(40,350),20)

print(n)
print(" ")

nSEARCH=int(input("Que numero desea buscar?\n"))

ocurrN= n.count(nSEARCH)

print(f"El numero {nSEARCH} tiene {ocurrN} numero de ocurrencias")

#EJERCICION N°6
from time import sleep

from time import sleep

segundos = 0
minutos = 0
horas = 0

while segundos < 60 :
    sleep(1)
    segundos += 1
    print(f"{horas} : {minutos} : {segundos}")
    if segundos == 60 :
        segundos = 0
        minutos += 1
        if minutos == 60 :
            minutos = 0
            horas += 1
            if horas == 24 :
                horas = 0
                minutos = 0
                segundos = 0
                break


#EJERCICIO N°7
from math import factorial

n = int(input("Ingrese su valor: "))

if n == 0 :
    print(1)
else :
    factor = n * factorial(n - 1)
    print(factor)

