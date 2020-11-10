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
x=' '

def mostrar_tablero():
    print('')
    print(4*x +'1', 3*x +'2', 3*x +'3')
    print('')
    print("A", 3*x+ gato_tablero["A1"], " | ", gato_tablero["A2"], " | ", gato_tablero["A3"])
    print(3*x +'--------------')
    print("B", 3*x+ gato_tablero["B1"], " | ", gato_tablero["B2"], " | ", gato_tablero["B3"],)
    print(3*x +'--------------')
    print("C", 3*x+ gato_tablero["C1"], " | ", gato_tablero["C2"], " | ", gato_tablero["C3"],)
    print('')
    print('')

mostrar_tablero()
#Ingresa un valor. Si la casilla esta vacía lo asigna. Si no, indica que la posición está ocupada y continua con el ciclo while.
while True:
    jugada1 = input("Ingrese su jugada: ")
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
if gato_tablero.get(jugada1) == "":
        gato_tablero[jugada1] = "X"
else:
    print("Posición ocupada")
mostrar_tablero()
jugada_cpu_1 = random.choice(alternativas)
print(jugada_cpu_1)
print(type(jugada_cpu_1))
if gato_tablero.get(jugada_cpu_1) == "":
    print("Esta posición está vacía")
    if jugada_cpu_1 == "A1":
        gato_tablero["A1"] = "O"
    elif jugada_cpu_1 == "A2":
        gato_tablero["A2"] = "O"
    elif jugada_cpu_1 == "A3":
        gato_tablero["A3"] = "O"
    elif jugada_cpu_1 == "B1":
        gato_tablero["B1"] = "O"
    elif jugada_cpu_1 == "B2":
        gato_tablero["B2"] = "O"
    elif jugada_cpu_1 == "B3":
        gato_tablero["B3"] = "O"
    elif jugada_cpu_1 == "C1":
        gato_tablero["C1"] = "O"
    elif jugada_cpu_1 == "C2":
        gato_tablero["C2"] = "O"
    elif jugada_cpu_1 == "C3":
        gato_tablero["C3"] = "O"
    else:
        print(jugada_cpu_1)
mostrar_tablero()
jugada1 = input("Ingrese su segunda jugada")
if jugada1 == "A1":
    gato_tablero["A1"] = "X"
elif jugada1 == "A2":
    gato_tablero["A2"] = "X"
elif jugada1 == "A3":
    gato_tablero["A3"] = "X"
elif jugada1 == "B1":
    gato_tablero["B1"] = "X"
elif jugada1 == "B2":
    gato_tablero["B2"] = "X"
elif jugada1 == "B3":
    gato_tablero["B3"] = "X"
elif jugada1 == "C1":
    gato_tablero["C1"] = "X"
elif jugada1 == "C2":
    gato_tablero["C2"] = "X"
elif jugada1 == "C3":
    gato_tablero["C3"] = "X"
mostrar_tablero()
alternativas = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
jugada_cpu_1 = random.choice(alternativas)
print(jugada_cpu_1)
print(type(jugada_cpu_1))
if gato_tablero.get(jugada_cpu_1) == "":
    print("Esta posición está vacía")
    if jugada_cpu_1 == "A1":
        gato_tablero["A1"] = "O"
    elif jugada_cpu_1 == "A2":
        gato_tablero["A2"] = "O"
    elif jugada_cpu_1 == "A3":
        gato_tablero["A3"] = "O"
    elif jugada_cpu_1 == "B1":
        gato_tablero["B1"] = "O"
    elif jugada_cpu_1 == "B2":
        gato_tablero["B2"] = "O"
    elif jugada_cpu_1 == "B3":
        gato_tablero["B3"] = "O"
    elif jugada_cpu_1 == "C1":
        gato_tablero["C1"] = "O"
    elif jugada_cpu_1 == "C2":
        gato_tablero["C2"] = "O"
    elif jugada_cpu_1 == "C3":
        gato_tablero["C3"] = "O"
    else:
        print(jugada_cpu_1)
mostrar_tablero()
'''
