
import sys

def pedirNumero(invitacion):
    while True:
        entrada = input(invitacion)
        try:
            entrada = int(entrada)
        except:
            print("Ha de escribir un numero.", file=sys.stderr)
        else:
            return entrada

def pedirNumeroAAdivinar(invitacion, max, min):
    invitacion = "\n" + invitacion
    invitacion += "\nEl numero ha de ser entre {} y {} incluidos: ".format(min,max)
    while True:
        entrada = pedirNumero(invitacion)
        if min <= entrada <= max:
            return entrada



print('######Introduzca el número a adivinar######')

minimo = maximo = 0

minimo = pedirNumero("Introduzca un numero minimo incluido: ")
maximo = pedirNumero("Introduzca un numero maximo incluido: ")
#comprobarEntrada(minimo, maximo)
numero = pedirNumeroAAdivinar("Introduzca numero a adivinar: ", maximo, minimo)

#Parte2
while True:
    intento = pedirNumero("Adivine el numero: ")
    if intento < numero:
        print('Más grande...')
    elif intento > numero:
        print('Más pequeño...')
    else:
        print('¡Has ganado!')
        break

sys.exit()

