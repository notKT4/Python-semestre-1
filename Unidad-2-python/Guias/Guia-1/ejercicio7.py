'''
7. Crear una lista con nombres de 5 trabajadores y otra lista con las edades de
estos 5 trabajadores, Se solicita relacionar ambas listas en una sola estructura.
La salida puede ser en tuplas o en un diccionario.

'''
nombres=["jose","juan","jorge","carlos","pato"]
edades=[28,37,40,36,89]

lista= {
    "1":(nombres[0],edades[0]),
    "2":(nombres[1],edades[1]),
    "3":(nombres[2],edades[2]),
    "4":(nombres[3],edades[3]),
    "5":(nombres[4],edades[4]),
}

tupla=(nombres[0],edades[0]),(nombres[1],edades[1]),(nombres[2],edades[2]),(nombres[3],edades[3]),(nombres[4],edades[4])

print(" ")
print(lista)
print(" ")
print(tupla)