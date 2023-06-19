'''
8. Elaborar un algoritmo que permita al usuario ingresar un mes y arroje la estacion
correspondiente a ese mes: verano, otoño, invierno o primavera.

'''
print(" ")
mes=input("Ingrese un mes \n")

print(" ")
print("El mes corresponde a la estacion: ")
print(" ")

if mes=="enero"or mes=="febrero"or mes=="diciembre":
    print("Verano")
elif mes=="marzo"or mes=="abril"or mes=="mayo":
    print("Otoño")
elif mes=="noviembre"or mes=="octubre"or mes=="septiembre":
    print("Primavera")
elif mes=="junio"or mes=="julio"or mes=="agosto":
    print("Invierno")
else:
    print("Porfavor ingrese un mes valido (Español)")

print(" ")