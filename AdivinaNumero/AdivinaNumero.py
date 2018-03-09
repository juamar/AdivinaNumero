
import sys

def pedirNumero():
    while True:
        numero = input('introduzca un numero entre 0 y 99: ')
        try:
            numero = int(numero)
        except:
            pass
    
        if 0 <= numero <= 99:
            break
    return numero

print('######Introduzca el número a adivinar######')

numero = pedirNumero()

#Parte2
while True:
    intento = pedirNumero()
    if intento < numero:
        print('Más grande...')
    elif intento > numero:
        print('Más pequeño...')
    else:
        print('¡Has ganado!')
        break

sys.exit()

