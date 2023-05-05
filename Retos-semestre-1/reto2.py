nombre = input("Ingrese el nombre del estudiante \n")
asig = input("Ingrese la asignatura del estudiante \n")
nota1 = float(input("Ingrese la nota del laboratorio nº1 \n"))
nota2 = float(input("Ingrese la nota del laboratorio nº2 \n"))

promedio = float(nota1 * 0.3) + (nota2 * 0.7)
dic = {
    "Nombre":nombre,
    "Asignatura":asig,
    "Nota lab 1":nota1,
    "Nota lab 2":nota2,
    "Promedio": round(promedio, 1)
}
