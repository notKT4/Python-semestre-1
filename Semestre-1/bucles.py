#01-WHILE
edad = 15
num = 0

#Bucle infinito
"""while edad < 18:
    print("Eres menor de edad, no puedes manejar")"""

#Bucle infinito
"""while True:
    print(num)
    num +=2"""

#Loop Infinito + Break
"""while True:
    parametro = input(">")
    if parametro == "exit":
        break
    else:
        print(parametro)"""

#Bucle For
#No esta bien optimizado
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)

print('FOR N°2')
newlista = [1,2,3,4,5,6,7,8,9,10]
for i in newlista:
    print(i)

print('FOR N°3')
for i in range(1,11):
    print(i)

print("################ 03 - ITERADOR E ITERABLES ################")
#Aprendiendo los conceptos de iterador e iterable
iterador = iter(newlista)

print(next(iterador))  #Imprime 1
print(next(iterador))  #Imprime 2
print(next(iterador))  #Imprime 3
print(next(iterador))  #Imprime 4
print(next(iterador))  #Impreme 5 ... y asi sucesivamente 