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

#SE PUEDEN SUMAR LISTAS?
print("Suma de listas",estudiantes+num)

#QUE HACEN ESTAS FUNCIONES?
print(list("Python"))
print(list(range(10)))
print("\n")

# - TUPLAS (NO MUTABLES)
newtupla = tuple()
grupo1 = ("Daniel","Cristian","Felipe",200,100,"Daniel")
print("########## 05-Tuplas ##########")
print (type(grupo1))

#ACCEDIENDO AL PRIMER ELEMENTO DE LA TUPLA
print(grupo1[0])

#MUESTRA EL INDICE DEL PRIMER ELEMENTO BUSCADO
print("Indice del elemento:",grupo1.index ("Daniel"))

#REASIGNANDO EL VALOR
grupo1[0] = "Constanza"
print(grupo1)

#SE PUEDEN SUMAR LAS TUPLAS?

#OBTENER UN TROZO DE LA TUPLA

grupo2 = ("Pedro",100,"Felipe","Diego",2020,"Alejandra")
print("Trozo de la tupla",grupo2[0:3])

#ENTONCES COMO NO PUEDO MODIFICAR UNA TUPLA, QUE PUEDO HACER?

grupo1 =list(grupo1)
print("La tupla ahora es de tipo:",type(grupo1,"\n"))

# - SETS (CONJUNTOS) - ESTRUCTURA FIJA
#FORMAS DE INICIALIZAR UN SET
print("########## 06-Sets ##########")
conjunto_vacio =set()
conjunto_vacio1 = {} #¿DICCIONARIO O SET?
print(type(conjunto_vacio1))
conjunto_colores = set({"Azul","Rojo","Verde"}) #UTILIZANDO LA FUNCION SET
conjunto_animales = {"Gato","Perro","Loro"} #UTILIZANDO LLAVES

print(type(conjunto_colores)) #TIPO DE DATO SET
print(type(conjunto_animales)) #TIPO DE DATO SET
print("El primer set contiene los siguientes colores:",conjunto_colores)
print("El segundo set contiene los siguientes animales:",conjunto_animales)

print(conjunto_animales[0]) #ACCEDIENDO AL PRIMER ELEMENTO DEL SET
conjunto_colores.add("Celeste")
print(conjunto_colores)

datos_personales = {
    "Nombre":"Victor",
    "Institucion":"Ulagos",
    "Edad": 29,
    "Asignaturas":{"Estructura de datos","Programacion"}
}

print("Diccionario inicial:",datos_personales)
print(len(datos_personales))

datos_personales["Institucion"] = "USS"
print("Diccionario actualizado:",datos_personales)

#AGREGANDO NUEVA CLAVE AL DICCIONARIO
datos_personales["Ciudad"] = "Osorno"
print(datos_personales)
print("Diccionario con el nuevo campo")