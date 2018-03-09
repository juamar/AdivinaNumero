
import sys

def MIN():
    return 0

def MAX():
    return 99

def pedirNumero(invitacion):
    invitacion += " entre "+str(MIN())+" y "+str(MAX())+": "
    while True:
        numero = input(invitacion)
        try:
            numero = int(numero)
        except:
            pass
    
        if MIN() <= numero <= MAX():
            break
    return numero

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

