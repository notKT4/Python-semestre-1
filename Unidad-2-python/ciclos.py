#BUCLES

#WHILE
num=0
while num <= 100:
    print(num)
    num +=2

#EJEMPLO DE BUCLE INFINITO(NO HACER O CORTAR DESPUES DE SU EJECUCION)
'''
while True:
    print(num)
    num +=2
'''
#WHILE CON ELSE-IF
while num <=100:
    print(num)
    num+=2
else:
    print("Mi condicion es igual o mayor a 100")

#LOOP INFINITO + DETENER BUCLE   
while True:
    parametro = input(">")
    if parametro == "exit":
        break
    else:
        print(parametro)


while num <= 300:
    print(num)
    num +=2
    if num ==250:
        print("Mi condicion es igual a 250")
print("Tercer bucle terminado")

while num <= 400:
    print(num)
    num +=2
    if num ==350:
        print("Se detiene la ejecucion")
        break
print(num)
print("Cuarto bucle terminado")

#USO DEL FOR

#NO ESTA BIEN OPTIMIZADO
print("EJEMPLO 1")
print(" ")
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)

#OPTIMIZADO
print("EJEMPLO 2")
print(" ")
lista=[1,2,3,4,5,6,7,8,9,10]

for i in lista:
    print (i)

#MAS OPTIMIZADO
print("EJEMPLO 3")
print(" ")
for i in range(11):
    print(i)