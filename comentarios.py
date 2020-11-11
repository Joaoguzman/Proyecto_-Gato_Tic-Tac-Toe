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
