'''
1. Obtener la cantidad de veces que se repite la palabra “universidad” dentro del siguiente
parrafo:
“La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion
democratica.”
Guardar las palabras encontradas dentro de una tupla.
'''

texto= """La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional 
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus 
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion
democratica""" 

quitar=",.;:\n!\""
for caracter in quitar:           
    texto=texto.replace(caracter,
                    "")   
texto=texto.lower()                     
v1=texto.count("universidad")
palabras=texto.split()
tupla1=tuple(palabras)     

print("la palabra universidad se repite",v1,"veces") 
#print(tupla2)    
print(tupla1) 
print(type(tupla1)) 