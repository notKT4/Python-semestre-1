#IF-ELSE

print("##### IF ELSE #####")
print(" ")

bencina = True
encendido = True
edad = 19

if bencina and encendido:
    print("Arranca")
else:
    print("No arranca")

if bencina or encendido:
    print("Arranca")
else:
    print("No arranca")

if not bencina or (encendido and edad >=18):
    print("Arranca")
else:
    print("No arranca")

print(" ")