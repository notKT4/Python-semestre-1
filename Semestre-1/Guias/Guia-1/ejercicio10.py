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

agenda={
    "nombre":"Jose",
    "direccion":"Cesar Ercilla 895",
    "ciudad":"Osorno",
    "numero telefonico":"+56945766687"
}

agenda["redes sociales"]= {
    "Facebook":"Jose Perez Cisterna",
    "Instagram":"jose_44",
    "Twitter":"joseperez_44"
}

print (agenda["redes sociales"]["Facebook"])
print (agenda)