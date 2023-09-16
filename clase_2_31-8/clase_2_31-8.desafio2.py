import random

nombres = ["Agumon", "Gabumon"]
hp = ["100","100"]
ataque = ["20", "18"]
movimientos = ["Patada", "Cabezazo", "Insultar a la madre", "Ultimate"]
movimientos_realizados_aliado = 0
movimientos_realizados_enemigo = 0
empatadas = 0
perdidas = 0
racha_actual = 0
racha_maxima = None
daño_del_ataque_aliado = 0
daño_del_ataque_aliado_critico = 0
daño_del_ataque_enemigo = 0
daño_del_ataque_enemigo_critico = 0
critico = 0
fue_critico_aliado = 0
fue_critico_enemigo = 0





print (f"\n\n\nComienza el juego.\n\n")
while int(hp[0]) > 0 and int(hp[1]) > 0:
    next_move = input(f"\nQue debería hacer a continuación {nombres[0]}? \
                    \n{movimientos[0]}. \n{movimientos[1]}. \n{movimientos[2]}. \n{movimientos[3]}.\n:").capitalize()
    
    if next_move not in movimientos:
        print("\n\nTipo inexistente. Ingrese un tipo valido.")
        continue

    if next_move == movimientos[3] and movimientos_realizados_aliado <= 3: 
        print("\n\nNecesitas realizas 3 movimientos antes de usar el ultimate. Selecciona otro movimiento.")
        continue

    print(f"\n{nombres[0]} elige: {next_move}")
    movimientos_realizados_aliado += 1

    opcion_cpu = random.choice(movimientos)
    while opcion_cpu == movimientos[3] and movimientos_realizados_enemigo <= 3: 
        opcion_cpu = random.choice(movimientos)
        
    print(f"{nombres[1]} eligió: {opcion_cpu}")
    movimientos_realizados_enemigo +=1



    fue_critico_aliado = 0
    critico = random.randint(0, 100)
    daño_del_ataque_aliado = random.randint(15,25)

    if critico > 95:
        daño_del_ataque_aliado_critico = daño_del_ataque_aliado * 2
        hp[1] = int(hp[1]) - daño_del_ataque_aliado_critico
        print("El ataque fue critico, el enemigo recibe el doble de daño.")
        fue_critico_aliado = 1
    else:
        hp[1] = int(hp[1]) - daño_del_ataque_aliado

    if int(hp[1]) <= 0:
        if fue_critico_aliado == 1:
            print(f"{nombres[1]} recibe un ataque CRITICO de {daño_del_ataque_aliado_critico} puntos y pierde todos sus puntos de vida restantes.")
        else:
            print(f"{nombres[1]} recibe un ataque de {daño_del_ataque_aliado} puntos y pierde todos sus puntos de vida restantes.")
    elif fue_critico_aliado == 1:
        print(f"{nombres[1]} recibe un ataque CRITICO de {daño_del_ataque_aliado_critico} puntos y queda con {hp[1]} puntos de vida.")
    else:
        print(f"{nombres[1]} recibe un ataque de {daño_del_ataque_aliado} puntos y queda con {hp[1]} puntos de vida.")



    fue_critico_enemigo = 0
    critico = random.randint(0, 100)
    daño_del_ataque_enemigo = random.randint(15,21)

    if critico > 95:
        daño_del_ataque_enemigo_critico = daño_del_ataque_enemigo * 2
        hp[0] = int(hp[0]) - daño_del_ataque_enemigo_critico
        print("El ataque fue critico, recibes el doble de daño.")
        fue_critico_enemigo = 1
    else:
        hp[0] = int(hp[0]) - daño_del_ataque_enemigo   

    if int(hp[0]) <= 0:
        if fue_critico_enemigo == 1:
            print(f"{nombres[0]} recibe un ataque CRITICO de {daño_del_ataque_enemigo_critico} puntos y pierde todos sus puntos de vida restantes.")
        else:
            print(f"{nombres[0]} recibe un ataque de {daño_del_ataque_enemigo} puntos y pierde todos sus puntos de vida restantes.")
    elif fue_critico_enemigo == 1:
        print(f"{nombres[0]} recibe un ataque CRITICO de {daño_del_ataque_enemigo_critico} puntos y queda con {hp[0]} puntos de vida.")
    else:
        print(f"{nombres[0]} recibe un ataque de {daño_del_ataque_enemigo} puntos y queda con {hp[0]} puntos de vida.")



    if int(hp[0]) < 0 or int(hp[1]) < 0:
        if int(hp[0]) < int(hp[1]):
            print(f"\nFin del juego. {nombres[1]} gana.")
        else:
            print(f"\nFin del juego. {nombres[0]} gana.")



#         empatadas += 1
#         racha_actual = 0
#     elif (next_move == tipos_pypets[0] and opcion_cpu == tipos_pypets[1] 
#         or next_move == tipos_pypets[1] and opcion_cpu == tipos_pypets[2]
#         or next_move == tipos_pypets[2] and opcion_cpu == tipos_pypets[0]):
#         mensaje = lista_resultados[0]
#         vidas += 1
#         ganadas += 1
#         racha_actual += 1
#     else:
#         mensaje = lista_resultados[1]
#         vidas -= 1
#         perdidas += 1
#         racha_actual = 0
    
#     if racha_maxima == None or racha_maxima < racha_actual:
#         racha_maxima = racha_actual

#     print(mensaje)
#     print(f"Te quedan {vidas} restantes y tu racha actual es {racha_actual}")
#     if vidas == vidas_maximas:
#         break
# informe=\
# f"""
# El resultado final es:
# Partidas ganadas {ganadas}
# Partidas perdidas {perdidas}
# Partidas empatadas {empatadas}
# Tu racha actual es {racha_actual}
# Y tu racha maxima fue {racha_maxima}
# """
# print (informe)