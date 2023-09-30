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


def stark_imprimir_nombres_alturas(lista_personajes: list[dict]) -> None:
    if type(lista_personajes) == list and len(lista_personajes) > 0:
        #if lista_personajes: #distinto de None, de 0, de False. Esta forma de validar no es suficiente
        for personaje in lista_personajes:
            print(obtener_nombre_y_dato(personaje, 'altura'))
    else: 
            return -1


def calcular_max(lista_personajes: list[dict], key: str) -> dict:
    lista_de_key = [] 
    for personaje in lista_personajes:
        for dato in personaje:
                if dato == key:
                    lista_de_key.append(float(personaje[dato]))
    key_maximo = max(lista_de_key)
    for personaje in lista_personajes:
        for dato in personaje:
            if dato == key:
                if float(personaje[dato]) == key_maximo:
                    personaje_maximo = personaje
            
    return personaje_maximo


def calcular_min(lista_personajes: list[dict], key: str) -> dict:
    lista_de_key = [] 
    for personaje in lista_personajes:
        for dato in personaje:
                if dato == key:
                    lista_de_key.append(float(personaje[dato]))
    key_minimo = min(lista_de_key)
    for personaje in lista_personajes:
        for dato in personaje:
            if dato == key:
                if float(personaje[dato]) == key_minimo:
                    personaje_minimo = personaje
            
    return personaje_minimo


def calcular_max_min_dato(lista_personajes: list[dict], max_o_min: str, key: str):
    if max_o_min == "maximo" or max_o_min == "max":
        superheroe_a_retornar = calcular_max(lista_personajes, key)
    elif max_o_min == "minimo" or max_o_min == "min":
        superheroe_a_retornar = calcular_min(lista_personajes, key)
    else:
        print("Error max o min")
        superheroe_a_retornar = -1

    return superheroe_a_retornar


def stark_calcular_imprimir_heroe(lista_personajes: list[dict], max_o_min: str, key: str):
    if type(lista_personajes) == list and len(lista_personajes) > 0:
        personaje_encontrado = calcular_max_min_dato(lista_personajes, max_o_min, key)
        mayor_menor_mensaje = {"maximo": "Mayor", "minimo": "Menor"}

        print(f"{mayor_menor_mensaje.get(max_o_min, 'ERROR')} {key}: {obtener_nombre_y_dato(personaje_encontrado, key)}")

    else:
        return -1


def sumar_dato_heroe(lista_personajes: list[dict], key: str) -> float:
    lista_datos = []
    for personaje in lista_personajes:
        if type(personaje) == dict and len(personaje) > 0:
            for dato in personaje:
                if dato == key:
                    lista_datos.append(float(personaje[dato]))
                    datos_sumados = sum(lista_datos)

    print(datos_sumados)


def dividir(dividendo: float, divisor: float) -> float:
    if not divisor == 0:
        resultado = dividendo / divisor
    else:
        resultado = 0

    return resultado




# Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de héroes y un string que representa el 
# dato del héroe que se requiere calcular el promedio. La función debe retornar el promedio del dato pasado por parámetro

def calcular_promedio(lista_personajes: list[dict], key: str) -> float:
    lista_datos = []
    for personaje in lista_personajes:
        for dato in personaje:
            if dato == key:
                lista_datos.append(personaje[dato])



# stark_normalizar_datos(lista_personajes)


# for personaje in lista_personajes:
#     for dato in personaje:
#         print(f"Tipo de dato: {type(personaje[dato])}, dato: {personaje[dato]}")


# for personaje in lista_personajes:
#     for dato in personaje:
#         print(f"Tipo de dato: {type(personaje[dato])}, dato: {personaje[dato]}")


# for personaje in lista_personajes:
#     print(obtener_nombre(personaje))


# stark_imprimir_nombres_heroes(lista_personajes)


# imprimir_dato(obtener_nombre_y_dato(lista_personajes[5], "altura"))


# stark_imprimir_nombres_alturas(lista_personajes) 


# print(calcular_max(lista_personajes, 'altura'))
# print(f"{obtener_nombre_y_dato(calcular_max(lista_personajes, 'altura'), 'altura')}")


# print(f"{obtener_nombre_y_dato(calcular_min(lista_personajes, 'peso'), 'peso')}")


# print(calcular_max_min_dato(lista_personajes, "maaximo", "peso"))


#stark_calcular_imprimir_heroe(lista_personajes, "maximo", "fuerza")


#sumar_dato_heroe(lista_personajes, "peso")


# print(dividir(155,0))



