import random
import time

gato_tablero = {
    "A1":"",
    "A2":"",
    "A3":"",
    "B1":"",
    "B2":"",
    "B3":"",
    "C1":"",   
    "C2":"",   
    "C3":"",   
}
alternativas = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

def mostrar_tablero():
    print("\t", "1\t", "2\t", "3\t")
    print("A", gato_tablero["A1"], "-  ", gato_tablero["A2"], "-  ", gato_tablero["A3"], "-  ")
    print("B", gato_tablero["B1"], "-  ", gato_tablero["B2"], "-  ", gato_tablero["B3"], "-  ")
    print("C", gato_tablero["C1"], "-  ", gato_tablero["C2"], "-  ", gato_tablero["C3"], "-  ")

mostrar_tablero()
'''
#Ingresa un valor. Si la casilla esta vacía lo asigna. Si no, indica que la posición está ocupada y continua con el ciclo while.
while True:
    jugada1 = input("Ingrese su jugada")
    if gato_tablero.get(jugada1) == "":
        gato_tablero[jugada1] = "X"
        break
    else:
        print("Posición ocupada")
        continue
#Se muestra el nuevo estado del tablero. 
mostrar_tablero()

#La CPU escoje un valor. 
while True:
    jugada_cpu_1 = random.choice(alternativas)
    time.sleep(3)
    if gato_tablero.get(jugada_cpu_1) == "":
        gato_tablero[jugada_cpu_1] = "O"
        break
    else:
        print("Posición ocupada")
        continue
mostrar_tablero()
'''
ficha_jugador=''
ficha_cpu=''

print("Bienvenido a GATO")
print("Usted se enfrentará a la CPU")
while True:
    ficha = input("Elija su ficha 'X' / 'O'")
    if ficha == 'X':
        ficha_jugador = ficha
        ficha_cpu = 'O'
        break
    elif ficha == 'O':
        ficha_jugador = ficha
        ficha_cpu = 'X'
        break
    else:
        print("Ficha equivocada, Intente Nuevamente")
        time.sleep(1)
        continue

if ficha_jugador == 'X' or ficha_jugador=='O':
    print("Su Ficha elegida es: ", ficha_jugador)
    print("La ficha de la cpu es: ", ficha_cpu)
    mostrar_tablero()
    input("Presione una Tecla para continuar...")

while True:
    mostrar_tablero()
    while True:
        print("El jugador", ficha_jugador ,"está en su jugada\n")
        jugada1 = input("Ingrese su jugada")
        if gato_tablero.get(jugada1) == "":
            gato_tablero[jugada1] = ficha_jugador
            break
        else:
            print("Posición ocupada")
            print("Vuelva a intentar")
            continue
    #COMPROBAR SI ES GANADOR
    while True:
        jugada_cpu_1 = random.choice(alternativas)
        time.sleep(3)
        if gato_tablero.get(jugada_cpu_1) == "":
            gato_tablero[jugada_cpu_1] = "O"
            break
        else:
            print("Posición ocupada")
            continue
    #COMPROBAR SI ES GANADOR