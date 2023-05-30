'''
Escribir una funcion que reciba una frase por teclado y 
devuelva un diccionario con las palabras que contiene
y su longitud
'''

'''
def obtener_longitud_palabras(frase):
    palabras = frase.split()
    diccionario = {}
    
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
    
    return diccionario

# Ejemplo de uso:
frase_usuario = input("Ingresa una frase: ")
resultado = obtener_longitud_palabras(frase_usuario)
print(resultado)

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



