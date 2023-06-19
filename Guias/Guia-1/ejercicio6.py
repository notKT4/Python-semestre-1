'''
Existen dos grupos de estudiantes de la carrera de Programacion que formaron
sus grupos para elaborar el Laboratorio N°3. Los grupos son los siguientes:
Grupo 1
Marcos
Gabriela
Benjamin
Matias

Grupo 2
Marcos
Nicolas
Diego
Matias
Se necesita saber si en ambos grupos tienen algun estudiante en comun y, en caso
de que asi sea, imprimir los nombres de esos estudiantes. Todo esto utilizando
Sets.
'''

grupo1 = {"Marcos", "Gabriela", "Benjamin", "Matias"}
grupo2 = {"Marcos", "Nicolas", "Diego", "Matias"}

estudiantes_en_comun = grupo1.intersection(grupo2)

if estudiantes_en_comun:
    print("Los estudiantes en común son:")
    for estudiante in estudiantes_en_comun:
        print(estudiante)
else:
    print("No hay estudiantes en común entre los dos grupos.")