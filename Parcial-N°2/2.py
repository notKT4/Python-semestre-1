'''
Calcular la media de calificaciones de la asignatura de Programación. Deducir cuántas son
más altas que la media y cuántas más bajas que dicha media. Se solicita un mínimo de 10
notas. Estas calificaciones se ingresarán por teclado y no se permite notas inferiores a 1.0 ni
mayores a 7.0.
'''
def calcular_media_notas():
    notas = []
    total_notas = 0
    cant_notas = 0

    # Solicitar y validar las notas ingresadas por el usuario
    while cant_notas < 10:
        nota = float(input("Ingrese una nota (entre 1.0 y 7.0): "))
        if nota < 1.0 or nota > 7.0:
            print("La nota ingresada está fuera del rango permitido.")
            continue

        notas.append(nota)
        total_notas += nota
        cant_notas += 1

    # Calcular la media de las notas
    media = total_notas / cant_notas

    # Determinar cuántas notas son más altas y cuántas son más bajas que la media
    notas_altas = 0
    notas_bajas = 0
    for nota in notas:
        if nota > media:
            notas_altas += 1
        elif nota < media:
            notas_bajas += 1

    return media, notas_altas, notas_bajas

# Llamar a la función para calcular la media de las notas y obtener las cantidades
media, cant_notas_altas, cant_notas_bajas = calcular_media_notas()

# Imprimir los resultados
print("La media de las calificaciones es:", media)
print("Cantidad de notas más altas que la media:", cant_notas_altas)
print("Cantidad de notas más bajas que la media:", cant_notas_bajas)


