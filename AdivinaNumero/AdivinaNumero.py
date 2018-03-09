
import sys

def pedirNumero(invitacion, min = 0, max = 99):
    invitacion += " entre "+str(min)+" y "+str(max)+": "
    while True:
        numero = input(invitacion)
        try:
            numero = int(numero)
            if min <= numero <= max:
                break
        except:
            pass
    return numero

print('######Introduzca el número a adivinar######')

numero = pedirNumero("Introduzca un numero")

#Parte2
while True:
    intento = pedirNumero("Adivine el numero", 0, 100)
    if intento < numero:
        print('Más grande...')
    elif intento > numero:
        print('Más pequeño...')
    else:
        print('¡Has ganado!')
        break

sys.exit()

