# import time
# tiempo_inicial = time.time()
# tiempo_final = time.time()
# resultado_tiempo = tiempo_final - tiempo_inicial
# print(resultado_tiempo)



# '''
# Crear una función que convierta grados Celsius a grados Fahrenheit. Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.
# '''
# def convertir_celsius_a_fahrenheit(celsius: float) -> float:
#     fahrenheit = celsius * (9/5) + 32
#     return fahrenheit

# celsius = float(input("Ingrese cantidad de grados celsius a convertir a fahrenheit: "))
# print(convertir_celsius_a_fahrenheit(celsius))



# '''
# Crear una función que calcule el área de un círculo. Recibe un parámetro (radio) y devuelve el área del círculo.
# '''
# def calcular_area_circulo(radio: float) -> float:
#     area_circulo = 3.14 * (radio*radio)
#     return area_circulo

# radio = float(input("Ingrese radio para calcular el area del circulo: "))
# print(calcular_area_circulo(radio))



# '''
# Crear una función que calcule el descuento aplicado a un producto. 
# Recibe dos parámetros (precio original y precio con descuento) y devuelve el porcentaje de descuento aplicado.
# '''
# def calcular_descuento_aplicado(precio_original: float, precio_con_descuento: float) -> float:
#     descuento = 100 - (precio_con_descuento * 100 / precio_original)
#     return descuento

# precio_original = int(input("Ingrese precio original: "))
# precio_con_descuento = int(input("Ingrese precio con descuento: "))
# descuento_aplicado = calcular_descuento_aplicado(precio_original, precio_con_descuento)
# print("Ejercicio 3: Descuento aplicado: {0}".format(descuento_aplicado))



# '''
# Crear una función que calcule el promedio de edad de un grupo de personas. Recibe una lista de edades y devuelve el promedio.
# '''
# def calcular_promedio_edades(lista_edades: list) -> float:
#     acumulador_edades = 0
#     for edad in lista_edades:
#         acumulador_edades += edad
#     promedio_edades = acumulador_edades/len(lista_edades)
#     #promedio_edades = sum(lista_edades)/len(lista_edades)
#     return promedio_edades

# lista_edades = [10, 20, 30, 40, 50, 55]
# promedio_edades = calcular_promedio_edades(lista_edades)
# print("Ejercicio 4: promedio de edades: {0}".format(promedio_edades))



# '''
# Crear una función que determine si un número es primo o no. Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.
# '''
# def determinar_numero_primo(numero_a_calcular: int) -> bool:
#     es_primo = True
#     for x in range(3, numero_a_calcular):
#         if numero_a_calcular % x == 0:
#             print(x)
#             es_primo = False
#     return es_primo

# numero_a_calcular = int(input("Ingrese numero a calcular: "))
# es_primo = determinar_numero_primo(numero_a_calcular)
# print(es_primo)
# if es_primo   == True:
#     print("Ejercicio 5: Es primo")
# else:
#     print("Ejercicio 5: No es primo")



# '''
# Crear una función que calcule el área de un triángulo. Recibe dos parámetros (base y altura) y devuelve el área.
# '''
# def calcular_area_triangulo(base:float, altura:float) -> float:
#     area_triangulo = (base * altura) / 2
#     return area_triangulo

# base = float(input("Ingrese base: "))
# altura = float(input("Ingrese altura: "))
# area_triangulo = calcular_area_triangulo(base, altura)
# print("Ejercicio 6: Area del triangulo: {0}".format(area_triangulo))



# '''
# Crear una función que calcule el máximo común divisor de dos números. Recibe dos parámetros (números) y devuelve el máximo común divisor.
# '''
# def calcular_maximo_comun_divisor(num1: int, num2: int) -> int:
#     maximo_comun_divisor = 1
#     for x in range(1, num2+1):
#         if num1 % x == 0:
#             if num2 % x == 0:
#                 maximo_comun_divisor = x
#     return maximo_comun_divisor

# num1 = int(input("Ingrese primer numero: "))
# num2 = int(input("Ingrese segundo numero: "))
# maximo_comun_divisor = calcular_maximo_comun_divisor(num1, num2)
# print("Ejercicio 7: Maximo comun divisor: {0}".format(maximo_comun_divisor))



# '''
# Crear una función que verifique si un número es par o impar. Recibe un número como parámetro y devuelve True si es par o False si es impar.
# '''
# def calcular_par_o_impar(numero: int) -> bool:
#     es_par = False
#     if numero % 2 == 0:
#         es_par = True
#     return es_par

# numero = int(input("Ingrese numero: "))
# es_par = calcular_par_o_impar(numero)
# print("Ejercicio 8: Es par: {0}".format(es_par))



# '''
# Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. 
# Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.
# '''
# def contar_repeticiones_de_elemento_en_lista(lista:list, elemento) -> int:
#     contador = 0
#     for x in lista:
#         if x == elemento:
#             contador += 1
#     return contador

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 2, 4, 5, 3, 5, 8, 6, 6, 6, 45, 1, 4, 9]
# elemento = int(input("Ingrese numero para buscarle repeticiones en la lista: "))
# repeticiones_de_elemento_en_lista = contar_repeticiones_de_elemento_en_lista(lista, elemento)
# print("Ejercicio 9: \nLista: {1}\nRepeticiones del elemento en la lista: {0}".format(repeticiones_de_elemento_en_lista, lista))



# '''
# Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.
# '''
# lista_de_palabras = [
#     "muercielago", "otorrinolaringologo", "auto", "pepsi"
#     ]

# def encuentra_palabra_mas_larga_de_la_lista(lista):
#     palabra_mas_larga = None

#     if lista_de_palabras: #esto significa: si tiene algo adentro, es true
#         for palabra in lista:
#             if palabra_mas_larga == None or len(palabra_mas_larga) < len(palabra):
#             #if not palabra_mas_larga: #si vale None, es como si fuera false. Al negarlo, se toma como true
#                 palabra_mas_larga = palabra
#     return palabra_mas_larga

# palabra_encontrada = encuentra_palabra_mas_larga_de_la_lista(lista_de_palabras)
# print(f"Ejercicio 10: La palabra mas larga es: {palabra_encontrada}")



# '''
# Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.
# '''
# def contar_vocales(cadena_de_texto:str) -> int:
#     vocales = ["a", "e", "i", "o", "u"]
#     contador = 0
#     for x in cadena_de_texto.lower():
#         if x in vocales:
#             contador += 1
#     return contador

# texto = f"Esta es una cadena de texto de ejemplo"
# print("Ejercicio 11: \nCadena de texto: {1}\nCantidad de vocales en la cadena de texto: {0}".format(contar_vocales(texto), texto))



# '''
# Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas
# '''
# def devolver_nombres_repetidos(lista_1: list, lista_2: list) -> list:
#     nombres_repetidos = []
#     for nombre in lista_1:
#         if nombre in lista_2:
#             nombres_repetidos.append(nombre)
#     return nombres_repetidos

# lista_1 = ["Pepe", "Moni", "Dardo", "Paola", "Naria", "Fatiga"]
# lista_2 = ["Pepe", "Juan", "Paola", "Marcos"]

# nombres_repetidos = devolver_nombres_repetidos(lista_1, lista_2)
# print("Ejercicio 12: Nombres repetidos: {0}".format(nombres_repetidos))



# '''
# Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores.
# '''
# def retorna_diccionario_palabras_y_cantidad_letras(lista_palabras: list[str]) -> dict[str, int]:
#     diccionario_palabras = {}
#     for palabra in lista_palabras:
#         diccionario_palabras[palabra] = len(palabra)

#     return diccionario_palabras

# lista_de_palabras = [
#     "muercielago", "otorrinolaringologo", "auto", "pepsi"
#     ]

# lista_personajes_c_c_h = [
#     "pepe", "moni", "dardo", "paola", "maria", "fatiga"
# ]

# diccionario_palabras_1 = retorna_diccionario_palabras_y_cantidad_letras(lista_de_palabras)
# print("Ejercicio 13: {0}".format(diccionario_palabras_1))

# diccionario_palabras_c_c_h = retorna_diccionario_palabras_y_cantidad_letras(lista_personajes_c_c_h)
# print(diccionario_palabras_c_c_h)

# for clave, valor in diccionario_palabras_c_c_h.items():
#     mensaje = f"La palabra: {clave} tiene {valor} letras."
#     print(mensaje)



# '''
# Crear una función que recibe una lista de números y devuelve un diccionario con el valor mínimo, el valor máximo y el promedio de los números en la lista.
# '''
# def devolver_min_max_promedio(lista_de_numeros:list) -> dict:
#     diccionario_min_max_promedio  = {}
#     flag = 0
#     min = None
#     max = None
#     promedio = 0
#     for numero in lista_de_numeros:
#         if flag == 0:
#             min = numero
#             max = numero
#             promedio = numero
#             flag = 1
#         elif numero < min:
#             min = numero
#         elif numero > max:
#             max = numero
#         promedio += numero
#     promedio = promedio / len(lista_de_numeros)

#     diccionario_min_max_promedio["minimo"] = min
#     diccionario_min_max_promedio["maximo"] = max
#     diccionario_min_max_promedio["promedio"] = promedio
#     return diccionario_min_max_promedio

# lista_de_numeros = [15, 23, 1, 1356, 35, 135]
# dict_min_max_prom = devolver_min_max_promedio(lista_de_numeros)
# print("Ejercicio 14: {0}".format(dict_min_max_prom))



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

    # for pelicula in lista_peliculas:
    #     genero = pelicula.get('genero', 'Sin genero')
    #     if not genero in informe_cantidades.keys():
    #         informe_cantidades[genero] = 1
    #     else:
    #         informe_cantidades[genero] += 1

    for pelicula in lista_peliculas:
        genero = pelicula.get('genero', 'Sin genero')

        informe_cantidades[genero] = informe_cantidades.get(genero, 0) + 1

    return informe_cantidades

informe = devuelve_cantidad_peliculas_por_genero(lista_peliculas)
print(informe)

