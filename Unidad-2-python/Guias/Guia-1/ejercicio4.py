'''
Elaborar un algoritmo que solicite al usuario su nombre y el nombre de otra
persona. Luego, mostrar en pantalla un mensaje que indique si ambos nombres
comienzan con la misma letra o si terminan con la misma letra, o si difieren tanto
en la letra inicial como en la final. Por ejemplo, si los nombres ingresados son
Belinda y Beatriz, se mostrara un mensaje que indique que ambos nombres comienzan con la misma letra. Si los nombres son Leonardo y Gonzalo, se mostrara
un mensaje que indique que ambos nombres terminan con la misma letra.
'''
nombre=str(input("Introduzca un nombre \n"))
nombre1=str(input("Introduzca un segundo nombre \n"))
if nombre[-1]==nombre1[-1] and nombre[0]==nombre1[0]:
    print("Ambos nombres terminan y empiezan con la misma letra")
elif nombre[-1]!=nombre1[-1] and nombre[0]!=nombre1[0]:
    print("Ambos nombres difieren tanto en la primera letra como la ultima")
elif nombre[0] == nombre1[0]:
    print("Ambos nombres comienzan con la misma letra.")
elif nombre[0]!=nombre1[0]: 
    print("Ambos nombres difieren en las iniciales")
elif nombre[-1]==nombre1[-1]:
    print("Ambos nombres terminan con la misma letra")
elif nombre[-1]!=nombre1[-1]:
    print("Ambos nombres difieren en la ultima letra")