'''
2. Escribir un programa que pida al usuario ingresar dos palabras y las guarde en
dos variables diferentes. Luego imprimir cual palabra tiene mas caracteres y cual
tiene menos caracteres.

'''

palabra =input("Ingrese una palabra \n")
palabra1 =input("Ingrese una segunda palabra \n")

if len(palabra) > len(palabra1):
    print(f"La palabra {palabra} tiene mas caracteres que la palabra {palabra1}")
elif len(palabra) < len(palabra1):
    print(f"La palabra {palabra1} tiene mas caracteres que la palabra {palabra}")
else:
    print(f"La palabra {palabra1} tiene la misma cantidad de caracteres que la palabra {palabra}")