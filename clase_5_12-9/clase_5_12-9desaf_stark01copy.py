from data_stark import lista_personajes

# # Esto 
# imprimir_personajes = list(filter(lambda x: x.get('genero') == 'F', lista_personajes))
# print(imprimir_personajes)

# # es equivalente a esto
# def filtrar_femeninos(personaje: dict) -> bool:
#     if personaje.get('genero') == 'F':
#         return True
#     return False

# imprimir_personajes =list(filter(filtrar_femeninos, lista_personajes))
# print(imprimir_personajes)









ejercicios_a_corregir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
mensaje_inicio = f'''
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
E. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
F. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
G. Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
H. Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia

Ingrese numero correspondiente a cada ejercicio:\n\
A: 1\n\
B: 2\n\
C: 3\n\
D: 4\n\
E: 5\n\
F: 6\n\
G: 7\n\
H: 8\n\
I: 9\n\
J: 10\n\
K: 11\n\
L: 12\n\
M: 13\n\
N: 14\n\
O: 15\n\
Salir: 16\n\n\
'''
continuar = None



def darle_valor_a_continuar(continuar: str) -> int:
    if(continuar == "no"):
        continuar = 1
    else:
        continuar = 2
    return continuar

def pedir_ejercicio_a_corregir(mensaje: str) -> int:
    opcion_elegida = int(input(mensaje))
    return opcion_elegida

def buscar_superheroe_mas_alto_por_genero(lista_personajes:list[dict], genero) -> dict:
    alturas = []
    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            alturas.append(float(personaje['altura']))

    altura_maxima = max(alturas)

    for personaje in lista_personajes:
        if float(personaje['altura']) == altura_maxima:
            personaje_mas_alto = personaje
    
    return personaje_mas_alto

def buscar_superheroe_mas_alto_bajo_por_genero(lista_personajes:list[dict], genero:str, alto:bool=True) -> dict:
    alturas = []
    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            alturas.append(float(personaje['altura']))

    if alto == True:
        altura_max_o_min = max(alturas)
    else:
        altura_max_o_min = min(alturas)

    for personaje in lista_personajes:
        if float(personaje['altura']) == altura_max_o_min:
            personaje_mas_alto_bajo = personaje
    
    return personaje_mas_alto_bajo

def buscar_promedio_altura_por_genero(lista_personajes:list[dict], genero:str) -> float:
    alturas = []
    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            alturas.append(float(personaje['altura']))

    promedio_alturas = sum(alturas)/len(alturas )

    return promedio_alturas



while continuar != "si" and continuar != "no":
    if continuar == None:
        continuar = input("\nQuiere corregir algun ejercicio? si/no: ")
    else:
        continuar = input("\nQuiere corregir otro ejercicio? si/no: ")
    if continuar != "si" and continuar != "no":
        continue

    continuar = darle_valor_a_continuar(continuar)


    match(continuar):
        case 1:
            print("chau")
            continuar = "no"

        case 2:
            opcion_elegida = pedir_ejercicio_a_corregir(mensaje_inicio)
            while opcion_elegida not in ejercicios_a_corregir:
                opcion_elegida = pedir_ejercicio_a_corregir(mensaje_inicio)

            match(opcion_elegida):
                case 1:
                    mensaje = "Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M"
                    print(f"Su eleccion fue A: {mensaje}")
                    imprimir_personajes = list(filter(lambda x: x.get('genero') == 'M', lista_personajes))
                    for personaje in imprimir_personajes:
                        print(personaje['nombre'])
                
                case 2:
                    mensaje = "Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F"
                    print(f"Su eleccion fue B: {mensaje}")
                    imprimir_personajes = list(filter(lambda x: x.get('genero') == 'F', lista_personajes))
                    for personaje in imprimir_personajes:
                        print(personaje['nombre'])
                
                case 3:
                    mensaje = "Recorrer la lista y determinar cuál es el superhéroe más alto de género M"
                    print(f"Su eleccion fue C: {mensaje}")                    
                    personaje_mas_alto = buscar_superheroe_mas_alto_bajo_por_genero(lista_personajes, 'M')
                    print(f"Superheroe genero M mas alto: {personaje_mas_alto['nombre']}, mide: {personaje_mas_alto['altura']}")

                case 4:
                    mensaje = "Recorrer la lista y determinar cuál es el superhéroe más alto de género F"
                    print(f"Su eleccion fue D: {mensaje}")
                    personaje_mas_alto = buscar_superheroe_mas_alto_bajo_por_genero(lista_personajes, 'F')
                    print(f"Superheroe genero F mas alto: {personaje_mas_alto['nombre']}, mide: {personaje_mas_alto['altura']}")

                case 5:
                    mensaje = "Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M"                    
                    print(f"Su eleccion fue E: {mensaje}")
                    personaje_mas_alto = buscar_superheroe_mas_alto_bajo_por_genero(lista_personajes, 'M', False)
                    print(f"Superheroe genero M mas bajo: {personaje_mas_alto['nombre']}, mide: {personaje_mas_alto['altura']}")

                case 6:
                    mensaje = "Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F"                    
                    print(f"Su eleccion fue F: {mensaje}")
                    personaje_mas_alto = buscar_superheroe_mas_alto_bajo_por_genero(lista_personajes, 'F', False)
                    print(f"Superheroe genero F mas bajo: {personaje_mas_alto['nombre']}, mide: {personaje_mas_alto['altura']}")

                case 7:
                    mensaje = "Recorrer la lista y determinar la altura promedio de los  superhéroes de género M"                    
                    print(f"Su eleccion fue G: {mensaje}")
                    promedio_alturas = buscar_promedio_altura_por_genero(lista_personajes, 'M')
                    print(f"Promedio de alturas de supereroes de genero M: {promedio_alturas}")

                case 8:
                    mensaje = "Recorrer la lista y determinar la altura promedio de los  superhéroes de género F"                    
                    print(f"Su eleccion fue H: {mensaje}")
                    promedio_alturas = buscar_promedio_altura_por_genero(lista_personajes, 'F')
                    print(f"Promedio de alturas de supereroes de genero F: {promedio_alturas}")
