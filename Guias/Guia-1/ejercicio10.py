'''
10. Crear una agenda telefonica que contenga un solo contacto. Esta agenda se debe
guardar en un diccionario. Este diccionario debe contar con las siguientes claves:
Nombre
Direccion
Ciudad
Numero telefonico
A continuacion, agrega una nueva clave llamada “Redes Sociales” que contenga al
menos tres nombres de perfil de diferentes redes sociales (por ejemplo, Facebook,
Instagram y Twitter). Por ultimo, se solicita imprimir solamente el Facebook del
contacto y luego la agenda completa actualizada.

'''

agenda = {
    "Nombre": "Juan Perez",
    "Direccion": "Calle Principal 123",
    "Ciudad": "Ciudad Ejemplo",
    "Numero telefonico": "1234567890"
}

agenda["Redes Sociales"] = ["Facebook: juanperez", "Instagram: juanperez_", "Twitter: @juanperez"]

print("Perfil de Facebook del contacto:", agenda["Redes Sociales"][0].split(": ")[1])

print("Agenda completa actualizada:")
for clave, valor in agenda.items():
    print(clave + ":", valor)
