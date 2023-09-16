
##################
# Hernan Potenza #
##################


import os




def darle_valor_a_continuar(continuar: str) -> int:
    '''
    Le da valor a la variable continuar para ver si se quier seguir corrigiendo ejercicios o no
    Recibe: la variable continuar
    Devuelve: la variable continuar con un valor entero
    '''
    if(continuar == "no"):
        continuar = 1
    else:
        continuar = 2
    return continuar


def pedir_ejercicio_a_corregir(mensaje: str) -> int:
    '''
    Pregunta que numero de ejercicio se quiere corregir
    Recibe: el mensaje a mostrar
    Devuelve: el numero de ejercicio que se quiere corregir
    '''
    opcion_elegida = int(input(mensaje))
    return opcion_elegida


def buscar_superheroe_mas_alto_bajo_por_genero(lista_personajes: list[dict], genero: str, alto: bool=True) -> dict:
    '''
    Busca el superheroe mas alto o bajo, segun el genero, que se pasa en la variable genero. Se elije si se busca el superheroe
    mas alto o el mas bajo segun el valor de la variable alto. Si alto es True, se busca el superheroe mas alto. Si no, el mas bajo
    Recibe: la lista con los personajes, el genero que se quiere buscar, y false si se quiere buscar al mas bajo
    Devuelve: un diccionario con todos los datos del superheroe elegido
    '''
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


def buscar_promedio_altura_por_genero(lista_personajes: list[dict], genero:str) -> float:
    '''
    Busca el promedio de altura segun el genero
    Recibe: lista de personajes y el genero a buscar
    Devuelve: el promedio de altura 
    '''
    alturas = []
    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            alturas.append(float(personaje['altura']))

    promedio_alturas = sum(alturas)/len(alturas )

    return promedio_alturas


def devuelve_cantidad_superheroe_por_color_ojos(lista_personajes: list[dict]) -> dict:        
    '''
    Busca y devuelve la cantidad de superheroe por cada grupo de color de ojos
    Recibe: lista de personajes
    Devuelve: un diccionario con los colores de ojo como clave y la cantidad de superheroes como valor
    '''
    informe_cantidades = {}

    for personaje in lista_personajes:
        color_ojos = personaje.get('color_ojos', 'No especifica color de ojos').capitalize()
        if not color_ojos in informe_cantidades.keys():
            informe_cantidades[color_ojos] = 1
        else:
            informe_cantidades[color_ojos] += 1

    return informe_cantidades


def devuelve_cantidad_superheroe_por_color_pelo(lista_personajes: list[dict]) -> dict:
    '''
    Busca y devuelve la cantidad de superheroe por color de pelo
    Recibe: lista de personajes
    Devuelve: un diccionario con los colores de pelo como clave y la cantidad de superheroes como valor
    '''   
    informe_cantidades = {}

    for personaje in lista_personajes:                
        color_pelo = personaje.get('color_pelo', 'No especifica color de pelo').capitalize()

        color_pelo = (lambda color_pelo: color_pelo if color_pelo != "" else "No especifica color de pelo")(color_pelo)
        informe_cantidades[color_pelo] = informe_cantidades.get(color_pelo, 0) + 1

    return informe_cantidades


def devuelve_cantidad_superheroe_por_inteligencia(lista_personajes: list[dict]) -> dict:        
    '''
    Busca y devuelve la cantidad de superheroe por cada grupo de tipo de inteligencia
    Recibe: lista de personajes
    Devuelve: un diccionario con los tipos de inteligencia como clave y la cantidad de superheroes como valor
    '''
    informe_cantidades = {}

    for personaje in lista_personajes:                
        inteligencia = personaje.get('inteligencia', 'No tiene').capitalize()

        inteligencia = (lambda inteligencia: inteligencia if inteligencia != "" else "No tiene")(inteligencia)
        informe_cantidades[inteligencia] = informe_cantidades.get(inteligencia, 0) + 1

    return informe_cantidades


def listar_cantidad_superheroe_por_color_ojos(lista_personajes: list[dict]) -> None:
    '''
    Lista la cantidad de superheroes por cada grupo de color de ojos
    Recibe: lista de personajes
    Devuelve: nada
    '''
    informe_cantidades = {}

    for personaje in lista_personajes:
        color_ojos = personaje.get('color_ojos', 'No especifica color de ojos').capitalize()
        nombre = personaje.get('nombre', 'No se sabe el nombre').capitalize()

        if not color_ojos in informe_cantidades.keys():
            informe_cantidades[color_ojos] = [nombre]
        else:
            informe_cantidades[color_ojos].append(nombre)

    print(informe_cantidades)


def listar_cantidad_superheroe_por_color_pelo(lista_personajes: list[dict]) -> None:     
    '''
    Lista la cantidad de superheroes por cada grupo de color de pelo
    Recibe: lista de personajes
    Devuelve: nada
    '''  
    informe_cantidades = {}

    for personaje in lista_personajes:
        color_pelo = personaje.get('color_pelo', 'No especifica color de pelo').capitalize()
        nombre = personaje.get('nombre', 'No se sabe el nombre').capitalize()

        if not color_pelo in informe_cantidades.keys():
            informe_cantidades[color_pelo] = [nombre]
        else:
            informe_cantidades[color_pelo].append(nombre)

    print(informe_cantidades)


def listar_cantidad_superheroe_por_tipo_inteligencia(lista_personajes: list[dict]) -> None:        
    '''
    Lista la cantidad de superheroes por cada grupo de tipo de inteligencia
    Recibe: lista de personajes
    Devuelve: nada
    '''
    informe_cantidades = {}

    for personaje in lista_personajes:
        inteligencia = personaje.get('inteligencia', 'No especifica tipo de inteligencia').capitalize()
        nombre = personaje.get('nombre', 'No se sabe el nombre').capitalize()

        if not inteligencia in informe_cantidades.keys():
            informe_cantidades[inteligencia] = [nombre]
        else:
            informe_cantidades[inteligencia].append(nombre)

    print(informe_cantidades)

def limpiar_consola() -> None:
    '''
    Limpia la consola
    Recibe: nada
    Devuelve: nada
    '''
    _ = input("\nPresione una tecla para continuar... ")
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.systenm('clear')
