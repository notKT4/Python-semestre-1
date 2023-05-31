lista_notas=(float(input("imprimir nota>"))) #imprimir notas y guardarlas en lista
nota= "x"

if nota<1.0 or nota>7.0:
    print("Nota no valida")

media=sum(lista_notas)/(len(lista_notas)) #dividido en el numero de notas

if nota>media:
    print("superior a la media")
else:
    print("inferior a la media")

