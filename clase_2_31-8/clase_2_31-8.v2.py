import random
#              0          1        2
opciones = ["Vaccine", "Virus", "Data"]
lista_mensajes = ["Gano el usuario", "Gano la maquina", "Hay un empate"]

while True: 
    jugador = input("Ingrese opcion: ").capitalize()
    if jugador not in opciones:
        print("opcion no valida, vuelva a ingresar opcion")
        continue

    maquina = random.choice(opciones)
    print(f"opcion elegida por maquina: {maquina}")

    if jugador == maquina:
        mensaje = lista_mensajes[2]
    elif (jugador == opciones[0] and maquina == opciones[1] 
        or jugador == opciones[1] and maquina == opciones[2]
        or jugador == opciones[2] and maquina == opciones[0]):
        mensaje = lista_mensajes[0]
    else:
        mensaje = lista_mensajes[1]
    print(mensaje)

    continuar = input("Desea continuar? s/n: ").lower()
    while continuar != 'n' and continuar != 's':
        continuar = input("Desea continuar? s/n: ").lower()
        
    if continuar == 'n':
        break




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
