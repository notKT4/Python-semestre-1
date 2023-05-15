lista = ["Santiago","Temuco","Osorno","Punta Arenas"]
lista2 = [134,99,245,50]

print(f"La ciudad con el indice de calidad de aire mas bajo es: {lista[2]}, con un ICA de {lista2[2]}")
print(f"La ciudad con el indice de calidad de aire mas alto es: {lista[3]}, con un ICA de {lista2[3]}")

ica1="Buena(ICA de 0 a 50)"
ica2="Moderada(ICA de 51 a100)"
ica3="Dañino a la salud para grupos sensibles(ICA de 101 a 150)"
ica4="Dañino a la salud(ICA de 151 a 200)"
ica5="Muy dañino a la salud(ICA de 201 a 300)"
ica6="Peligroso(ICA superior a 300)"

print(f"EL ICA de {lista[2]} es: {ica5}")
print(f"El ICA de {lista[3]} es: {ica1}")