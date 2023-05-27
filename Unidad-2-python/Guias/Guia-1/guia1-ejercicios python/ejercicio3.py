'''
3. Tres empleados de una fabrica trabajan en dos turnos: diurno y nocturno (10 hrs cada
uno). Se busca calcular el pago diario y el total semanal de cada empleado de acuerdo
con los siguientes puntos:
a) La tarifa del turno diurno por hora es de 12000 CLP.
b) La tarifa del turno nocturno por hora es de 16000 CLP.
c) Los domingos la tarifa se incrementa en 2000 CLP el turno diurno y 3000 CLP el
turno nocturno.
Ademas considerar:
a) El primer empleado trabaja Lunes, Martes y Miercoles en turnos nocturnos, Jueves
y Viernes en turnos diurnos.
b) El segundo empleado trabaja Martes, Miercoles y Jueves turnos nocturnos, y tambien 
el dia domingo en turno diurno.
c) El tercer empleado trabaja Miercoles, Jueves y Viernes diurno, Sabado y Domingo 
en turnos nocturnos.
Guardar la informacion de cada empleado en un diccionario, con el pago diario que debe
recibir cada empleado y el total de la semana.

'''

#ALGORITMO EMPLEADOS

Tdiurno = 12000
Tnocturno = 16000

domD= Tdiurno+2000
domN= Tnocturno+3000

print("Pago diario empleado 1")
emp1={
    "Lunes":Tnocturno*10,
    "Martes":Tnocturno*10,
    "Miercoles":Tnocturno*10,
    "Jueves":Tdiurno*10,
    "Viernes":Tdiurno*10,
}
print(emp1)
print(" ")

print("Pago diario empleado 2")
emp2={
    "Martes":Tnocturno*10,
    "Miercoles":Tnocturno*10,
    "Jueves":Tdiurno*10,
    "Domingo":domD*10,
}
print(emp2)
print(" ")

print("Pago diario empleado 3")
emp3={
    "Sabado":Tnocturno*10,
    "Domingo":domN*10,
    "Miercoles":Tnocturno*10,
    "Jueves":Tdiurno*10,
    "Viernes":Tdiurno*10,
}
print(emp3)
print(" ")

tsemanal1=sum(emp1.values())
tsemanal2=sum(emp2.values())
tsemanal3=sum(emp3.values())

tsemanal={
    "Empleado1":tsemanal1,
    "Empleado2":tsemanal2,
    "Empleado3":tsemanal3,
}

print("Ls tarifas semanales son: \n")
print(tsemanal)
print(" ")