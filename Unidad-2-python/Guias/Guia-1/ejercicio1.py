'''
1.REALIZAR UN ALGORITMO QUE INDIQUE EL NUMERO MENOR Y EL NUMERO MAYOR ENTRE TRES ENTEROS
LEIDOS POR CONSOLA. SOLO SE DEBEN INGRESAR NUMEROS ENTEROS

'''
print("Numero mayor y menor entre 3 numeros (Solo enteros)")

n1= input("Ingrese un numero (a) \n")
n2= input("Ingrese un segundo numero (b) \n")
n3= input("Ingrese un tercer numero (c) \n")

n = n1,n2,n3

if n != int:
    print("Un numero no es valido, ingrese solo numeros enteros")

if n == int:
    if n1>n2>n3:
        print("a>b>c")
    if n1>n3>n2:
        print("a>c>b")
    if n2>n3>n1:
        print("b>c>a")
    if n2>n1>n3:
        print("b>a>c")
    if n3>n2>n1:
        print("c>b>a")
    if n3>n1>n2:
        print("c>a>b")