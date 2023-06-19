'''
Escribir una funcion que reciba una frase por teclado y 
devuelva un diccionario con las palabras que contiene
y su longitud
'''

def long(frase):
    palabras= frase.split()
    dict= {}

    for palabra in palabras:
        dict[palabra]=len(palabra)

    return dict

frase=str(input("Ingrese una frase \n"))
funcion= long(frase)

print(funcion)



