'''
Crear un algoritmo que solicite por consola las 3 notas de los laboratorios realizados en el ramo de Programacion. Luego obtener el promedio ponderado de la
siguiente manera:
Promedio Ponderado = Lab1 * 0,3 + Lab2 * 0,4 + Lab3 * 0,3
Si el promedio es menor a 4,0 debe imprimir el mensaje que el estudiante reprobo
la asignatura. Si el promedio es superior a 4,0, indicar que el estudiante aprobo
la asignatura. Si la nota es superior 6,0, debe mostrar el mensaje: el estudiante
aprobo con distincion.

'''
lab1=float(input("Ingrese la nota del laboratorio 1 \n"))
lab2=float(input("Ingrese la nota del laboratorio 2 \n"))
lab3=float(input("Ingrese la nota del laboratorio 3 \n"))

Promedio_ponderado= lab1 * 0.3 + lab2 * 0.4 + lab3 * 0.3

if Promedio_ponderado >= 4.0 and Promedio_ponderado < 6.0:
    print("El estudiante aprobo")
elif Promedio_ponderado < 4.0:
    print("El estudiante reprobo")
else: print("El estudiante aprobo con distincion")
