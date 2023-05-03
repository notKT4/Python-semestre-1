#TIPOS DE DATOS
#1.Datos de tipo numerico

edad = 29 #entero
estatura = 1.71 #real
peso = 70.5
complejo = 1 + 4j #complejo

#TRANSFORMANDO DE REAL A ENTERO
print (peso)
print ("Transformando un valor real a entero:",int(peso))

#TRANSFORMANDO DE ENTERO A REAL
print ("Transformando un valor entero a real:",float(edad))

#OPERACION ARITMETICA BASICA
imc = peso / (estatura**2)
print("Mi IMC es de:",imc,"\n")

print("Mi IMC es de: {:.2f}".format(imc),"\n") #FORMATEANDO EL VALOR

#2. DATOS DE TIPO CADENA DE CARACTERES
asignatura = "Programacion"
carrera = "Ingenieria civil en informatica"

print("######## 02-STRINGS ########")
print("La asignatura de ",asignatura,"corresponde a la carrera de",carrera)

#UTILIZANDO LA FUNCION LEN (CUENTA LA CANTIDAD DE CARACTERES)

print("La cantidad de caracteres de la palabra",asignatura,"es de:",len(asignatura))
print("La cantidad de caracteres de la palabra",carrera,"es de:",len(carrera))

#3. VALORES BOOLEANOS

ampolleta = False
interruptor = True

print("######## 03-BOOLEANS ########")
print(ampolleta,interruptor)

#PODEMOS TRANSFORMAR CULAQUIER VALOR A UN BOOLEANO (al igual que un string, int, etc.)
print(bool(0))
print(bool(None))
print(bool(True))
print(bool(1))

#INICIALIZANDO LISTAS DE 2 MANERAS
nueva_lista =list()

#DECLARANDO TRES LISTAS DIFERENTES
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian", "Marco"]
num = [1,2,3,4,5,6]
lenguaje = ["Python"]

#SE PUEDE REALIZAR UNA LISTA DE DATOS COMPUESTOS
data = ["Osorno", {"UV" : "nivel bajo", "temp C" :15}, (-40.5727, 73.1353)]
listamixta = ["Felipe", 100, True]

print("lista de caden de caracteres:",estudiantes)
print("lista de numeros:", num)
print("lista de ")
print("Esto igual es una lista:",data)
print(len(listamixta)) #PARA SABER LA CANTIDAD DE ELEMENTOS DE UNA LISTA
print(estudiantes.count("PEPE"))
print(num.count(5000)) #CANTIDAD DE OCURRENCIAS DE UN ELEMENTO EN ESPECIFICO

lenguaje = ["JavaScript"]
print("Nuevo valor de Arreglo de un elemento:",lenguaje)

#COMO ACCEDO A UN ELEMENTO ESPECIFICO DE LA LISTA?

print(estudiantes[0]) #CORRECTO (1ER ELEMENTO DE LA LISTA)
print(estudiantes[1]) #2DO ELEMENTO DE LA LISTA
print("Posicion -2",estudiantes[-2])