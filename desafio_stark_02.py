from data_stark import lista_personajes


'''    
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
'''

def stark_normalizar_datos(lista_personajes: list[dict]) -> None:
    '''
    Recorre la lista y convierte al tipo de dato correcto los datos numericos. imprime "datos normalizados" si al menos un dato fue modificado,
    si no modifico ningun dato, no imprime nada. Si la lista esta vacia imprime "Error: Lista de héroes vacía"
    Recibe: lista de personajes
    Devuelve: nada
    '''
    flag = 0
    dato_a_normalizar = ["altura", "peso", "fuerza"]
    if lista_personajes:
        for personaje in lista_personajes:
            for dato in personaje:
                if dato in dato_a_normalizar:
                    personaje[dato] = float(personaje[dato])
                    flag = 1
    else:
        print("Error: Lista de héroes vacía")
    
    if flag == 1:
        print("Datos normalizados")


def obtener_nombre(personaje: dict) -> str:
    '''
    Devuelve el nombre del personaje con el formato correcto
    Recibe: el diccionario de un personaje
    Devuelve: string con el nombre formateado
    '''
    for dato in personaje:
        if dato == "nombre":
            nombre_formateado = f"Nombre: {personaje[dato]}"

    return nombre_formateado


def imprimir_dato(dato_a_imprimir: str) -> None:
    '''
    Imprime el dato en consola
    Recibe: el dato a imprimir
    Devuelve: nada
    '''
    print(dato_a_imprimir)


def stark_imprimir_nombres_heroes(lista_personajes: list) -> None:
    '''
    Imprime en consola los nombres de los heroes
    Recibe: lista de personajes
    Devuelve: nada
    '''
    if lista_personajes:
        for personaje in lista_personajes:
            imprimir_dato(obtener_nombre(personaje))
    else:
        return -1


def obtener_nombre_y_dato(personaje: dict, key: str) -> str:
    for dato in personaje:
        if dato == key:
            nombre_y_dato = f"Nombre: {personaje['nombre']} | {key}: {personaje[key]}"
    
    return nombre_y_dato


# Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por parámetro la lista de héroes, 
# la cual deberá iterar e imprimir sus nombres y alturas USANDO la función creada en el punto 2. Validar que la lista de 
# héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
# Con este se resuelve el Ej 2 del desafío #00


def stark_imprimir_nombres_alturas(lista_personajes: list) -> None:
    if type(lista_personajes) == list and len(lista_personajes) > 0:
        #if lista_personajes: #distinto de None, de 0, de False
            for personaje in lista_personajes:
                obtener_nombre_y_dato(personaje, 'altura')
    else: 
            print("awfasfasf")






stark_imprimir_nombres_alturas(lista)


# imprimir_dato(obtener_nombre_y_dato(lista_personajes[5], "altura"))

# stark_imprimir_nombres_heroes(lista_personajes)

# for personaje in lista_personajes:
#     for dato in personaje:
#         print(f"Tipo de dato: {type(personaje[dato])}, dato: {personaje[dato]}")

# stark_normalizar_datos(lista_personajes)

# for personaje in lista_personajes:
#     for dato in personaje:
#         print(f"Tipo de dato: {type(personaje[dato])}, dato: {personaje[dato]}")

# for personaje in lista_personajes:
#     print(obtener_nombre(personaje))