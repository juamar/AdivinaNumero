
import sys

#Parte1
print('######Introduzca el número a adivinar######')
while True:
    numero = input('introduzca un numero entre 0 y 99: ')
    try:
        numero = int(numero)
    except:
        pass
    
    if 0 <= numero <= 99:
        break

#Parte2
while True:
    while True:
        intento = input('introduzca un número entre 0 y 99: ')
        try:
            intento = int(intento)
        except:
            pass
        if 0 <= numero <= 99:
            break
    if intento < numero:
        print('Más grande...')
    elif intento > numero:
        print('Más pequeño...')
    else:
        print('¡Has ganado!')
        break

sys.exit()

