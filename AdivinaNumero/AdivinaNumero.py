
import sys

def MIN():
    return 0

def MAX():
    return 99

print('######Introduzca el número a adivinar######')

numero = pedirNumero("Introduzca un numero")

#Parte2
while True:
    intento = pedirNumero("Adivine el numero")
    if intento < numero:
        print('Más grande...')
    elif intento > numero:
        print('Más pequeño...')
    else:
        print('¡Has ganado!')
        break

sys.exit()

def pedirNumero(invitacion):
    invitacion += " entre "+str(MIN())+" y "+str(MAX())+": "
    while True:
        numero = input(invitacion)
        try:
            numero = int(numero)
            if MIN() <= numero <= MAX():
                break
        except:
            pass
    return numero
