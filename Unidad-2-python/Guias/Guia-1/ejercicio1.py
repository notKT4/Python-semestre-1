'''
1.REALIZAR UN ALGORITMO QUE INDIQUE EL NUMERO MENOR Y EL NUMERO MAYOR ENTRE TRES ENTEROS
LEIDOS POR CONSOLA. SOLO SE DEBEN INGRESAR NUMEROS ENTEROS

'''
print("Numero mayor y menor entre 3 numeros (Solo enteros)")

n1= (input("Ingrese un numero (a) \n"))
n2= (input("Ingrese un segundo numero (b) \n"))
n3= (input("Ingrese un tercer numero (c) \n"))

if n1==n2==n3:
    print("Los tres numeros son iguales")
else:
    print("El numero mayor es: ")
    print (max(n1,n2,n3))
    print("El numero menor es: ")
    print(min(n1,n2,n3))
