
##################
# Hernan Potenza #
##################


ejercicios_a_corregir = [10, 11, 12, 13, 14, 15]
opcion = int(input("Ingrese numero de ejercicio, del 10 al 15: "))
while opcion not in ejercicios_a_corregir:
    opcion = int(input("Ingrese numero de ejercicio, del 10 al 15 dije: "))

match(opcion):
    case 10:
        '''
        Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.
        '''
        lista_de_palabras = [
            "muercielago", "otorrinolaringologo", "auto", "pepsi"
            ]

        def encuentra_palabra_mas_larga_de_la_lista(lista):
            palabra_mas_larga = None

            if lista_de_palabras: #esto significa: si tiene algo adentro, es true
                for palabra in lista:
                    if palabra_mas_larga == None or len(palabra_mas_larga) < len(palabra):
                    #if not palabra_mas_larga: #si vale None, es como si fuera false. Al negarlo, se toma como true
                        palabra_mas_larga = palabra
            return palabra_mas_larga

        palabra_encontrada = encuentra_palabra_mas_larga_de_la_lista(lista_de_palabras)
        print(f"Ejercicio 10: La palabra mas larga es: {palabra_encontrada}")

    case 11:
        '''
        Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.
        '''
        def contar_vocales(cadena_de_texto:str) -> int:
            vocales = ["a", "e", "i", "o", "u"]
            contador = 0
            for x in cadena_de_texto.lower():
                if x in vocales:
                    contador += 1
            return contador

        texto = f"Esta es una cadena de texto de ejemplo"
        print("Ejercicio 11: \nCadena de texto: {1}\nCantidad de vocales en la cadena de texto: {0}".format(contar_vocales(texto), texto))

    case 12:
        '''
        Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas
        '''
        def devolver_nombres_repetidos(lista_1: list, lista_2: list) -> list:
            nombres_repetidos = []
            for nombre in lista_1:
                if nombre in lista_2:
                    nombres_repetidos.append(nombre)
            return nombres_repetidos

        lista_1 = ["Pepe", "Moni", "Dardo", "Paola", "Naria", "Fatiga"]
        lista_2 = ["Pepe", "Juan", "Paola", "Marcos"]

        nombres_repetidos = devolver_nombres_repetidos(lista_1, lista_2)
        print("Ejercicio 12: Nombres repetidos: {0}".format(nombres_repetidos))


    case 13:
        '''
        Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores.
        '''
        def retorna_diccionario_palabras_y_cantidad_letras(lista_palabras: list[str]) -> dict[str, int]:
            diccionario_palabras = {}
            for palabra in lista_palabras:
                diccionario_palabras[palabra] = len(palabra)

            return diccionario_palabras

        lista_personajes_c_c_h = [
            "pepe", "moni", "dardo", "paola", "maria", "fatiga"
        ]

        diccionario_palabras_c_c_h = retorna_diccionario_palabras_y_cantidad_letras(lista_personajes_c_c_h)

        print("Ejercicio 14:")
        for clave, valor in diccionario_palabras_c_c_h.items():
            mensaje = f"La palabra: {clave} tiene {valor} letras."
            print(mensaje)



    case 14:
        '''
        Crear una función que recibe una lista de números y devuelve un diccionario con el valor mínimo, el valor máximo y el promedio de los números en la lista.
        '''
        def devolver_min_max_promedio(lista_de_numeros:list) -> dict:
            diccionario_min_max_promedio  = {}
            flag = 0
            min = None
            max = None
            promedio = 0
            for numero in lista_de_numeros:
                if flag == 0:
                    min = numero
                    max = numero
                    promedio = numero
                    flag = 1
                elif numero < min:
                    min = numero
                elif numero > max:
                    max = numero
                promedio += numero
            promedio = promedio / len(lista_de_numeros)

            diccionario_min_max_promedio["minimo"] = min
            diccionario_min_max_promedio["maximo"] = max
            diccionario_min_max_promedio["promedio"] = promedio
            return diccionario_min_max_promedio

        lista_de_numeros = [15, 23, 1, 1356, 35, 135]
        dict_min_max_prom = devolver_min_max_promedio(lista_de_numeros)
        print("Ejercicio 14: {0}".format(dict_min_max_prom))


    case 15:
        '''
        Crear una función que recibe una lista de diccionarios con información de películas (título, género, director) 
        y devuelve un diccionario con la cantidad de películas por género.
        '''
        lista_peliculas = [
            {
                "titulo": "Transformers 1",
                "genero": "Accion",
                "director": "Michael Bay"
            },
            {
                "titulo": "Transformers 2",
                "genero": "Accion",
                "director": "Michael Bay"
            },
            {
                "titulo": "Transformers 3",
                "genero": "Accion",
                "director": "Michael Bay"
            },
            {
                "titulo": "El juego del miedo",
                "genero": "Terror",
                "director": "El viejito del saw"
            },
            {
                "titulo": "El juego del miedo 2",
                "genero": "Terror",
                "director": "El viejito del saw"
            },
            {
                "titulo": "Black Clover",
                "genero": "Animation",
                "director": "Un japones director"
            },
            {
                "titulo": "One Piece",
                "director": "Otro japones director"
            },
        ]

        def devuelve_cantidad_peliculas_por_genero(lista_peliculas: list[dict]) -> dict:        
            informe_cantidades = {}
        
            for pelicula in lista_peliculas:
                genero = pelicula.get('genero', 'Sin genero')
                if not genero in informe_cantidades.keys():
                    informe_cantidades[genero] = 1
                else:
                    informe_cantidades[genero] += 1
        
            # for pelicula in lista_peliculas:
            #     genero = pelicula.get('genero', 'Sin genero')
        
            #     informe_cantidades[genero] = informe_cantidades.get(genero, 0) + 1
        
            return informe_cantidades
        
        informe = devuelve_cantidad_peliculas_por_genero(lista_peliculas)
        print(informe)