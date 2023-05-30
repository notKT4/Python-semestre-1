'''
Obtener los números del rango 10 al 30,
incrementando de 2 en 2. A continuación,
sumar todos los números obtenidos.
'''
suma=0

for i in range(10,31):
    while i < 30:
        print(i)
        i +=2
        suma+= i
    if i ==30:
        print("30")
        print("Se detiene la ejecucion")
        break
print(f"la suma de todos los numeros es igual a: {suma}")
