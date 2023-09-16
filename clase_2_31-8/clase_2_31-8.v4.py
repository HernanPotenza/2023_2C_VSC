import random
#              0          1        2
opciones = ["Vaccine", "Virus", "Data"]
lista_mensajes = ["Gano el usuario", "Gano la maquina", "Hay un empate"]
vidas = 3
partidas_ganadas = 0
partidas_perdidas = 0
partidas_empatadas = 0
racha = False

print(f"Comienza el juego. Tenes {vidas} vidas")
while vidas > 0: 
    jugador = input("Ingrese opcion: ").capitalize()
    if jugador not in opciones:
        print("opcion no valida, vuelva a ingresar opcion")
        continue
    print(f"opcion elegida por jugador: {jugador}")

    maquina = random.choice(opciones)
    print(f"opcion elegida por maquina: {maquina}")

    if jugador == maquina:
        mensaje = lista_mensajes[2]
        partidas_empatadas += 1
        racha = False
    elif (jugador == opciones[0] and maquina == opciones[1] 
        or jugador == opciones[1] and maquina == opciones[2]
        or jugador == opciones[2] and maquina == opciones[0]):
        mensaje = lista_mensajes[0]
        vidas += 1
        partidas_ganadas += 1
        if racha == False:
            racha = True
        else:
            break
    else:
        mensaje = lista_mensajes[1]
        vidas -= 1
        partidas_perdidas += 1
        racha = False

    print(mensaje)
    print(f"Te quedan {vidas} vidas restantes")
    if vidas == 5:
        break

informe = (f"\nGanaste {partidas_ganadas} partidas y perdiste {partidas_perdidas}")

informe2 =\
f"""
El resultado final es:
Partidas ganadas: {partidas_ganadas}.
Partidas perdidas: {partidas_perdidas}.
Partidas empatadas: {partidas_empatadas}.
"""

print (informe)
print (informe2)



    # elif jugador == opciones[0]:
    #     if maquina == opciones[1]:
    #         mensaje = lista_mensajes[0]
    #     else:
    #         mensaje = lista_mensajes[1]
    
    # elif jugador == opciones[1]:
    #     if maquina == opciones[2]:
    #         mensaje = lista_mensajes[0]
    #     else:
    #         mensaje = lista_mensajes[1]

    # elif jugador == opciones[2]:
    #     if maquina == opciones[0]:
    #         mensaje = lista_mensajes[0]
    #     else:
    #         mensaje = lista_mensajes[1]
    # print(mensaje)
