'''
6. Simular el comportamiento de un reloj digital, imprimiendo la hora, minutos y segundos
de un dia desde las 00:00:00 horas hasta las 23:59:59 horas.

'''

from time import sleep

from time import sleep

segundos = 0
minutos = 0
horas = 0

while segundos < 60 :
    sleep(1)
    segundos += 1
    print(f"{horas} : {minutos} : {segundos}")
    if segundos == 60 :
        segundos = 0
        minutos += 1
        if minutos == 60 :
            minutos = 0
            horas += 1
            if horas == 24 :
                horas = 0
                minutos = 0
                segundos = 0
                break