
# # 2


# GUIA EJERCICIOS BASICOS CON STRINGS

# 1 - Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.
# # cadena_mayusculas = lambda cadena: cadena.upper()
# # print(cadena_mayusculas("hola"))

# 2 - Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.
# # cadena_minusculas = lambda cadena: cadena.lower()
# # print(cadena_minusculas("hOLa"))

# 3 - Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, separados por un espacio.
# cadenas_concatenadas = lambda palabra_1, palabra_2: f"{palabra_1} {palabra_2}"
# print(cadenas_concatenadas("Hola", "TARAAA"))

# def conectar_con_espacios(nombre_1: str, nombre_2: str) -> str:
#     lista_nombres = [nombre_1, nombre_2]
#     nombres = ' '.join(lista_nombres)
#     return nombres

# print(conectar_con_espacios("Juan", "Pedro"))

# def concatenar_cadenas(cadena_1, cadena_2):
#     return cadena_1 + " " + cadena_2

# cadena = concatenar_cadenas("Juan", "Pedro")
# print(cadena)

# def concatenar_cadenas_2(cadena_1, cadena_2):
#     mensaje = "{0} {1}".format(cadena_1, cadena_2)
#     return mensaje

# def concatenar_cadenas_3(cadena_1, cadena_2):
#     mensaje = f"{cadena_1} {cadena_2}"
#     return mensaje

# def concatenar_cadenas_4(cadena_1, cadena_2):
#     lista_de_cadenas = [cadena_1, cadena_2]
#     cadena_final = " ".join(lista_de_cadenas)
#     return cadena_final

# cadena = concatenar_cadenas_4("Juan", "Pedro")
# print(cadena)

# 4 - Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.
# def contar_caracteres(cadena:str) -> str:
#     return len(cadena)

# cantidad_caracteres = contar_caracteres("Hola mundo")
# print(cantidad_caracteres)

# 5 - Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.
# def contar_aparicion_de_caracteres(cadena:str, caracter:str) -> str:
#     return cadena.count(caracter)

# aparicion_caracter = contar_aparicion_de_caracteres("Hola mundo", "o")
# print(aparicion_caracter)

# 6 -Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que contienen ese carácter.
# def muestra_palabra_con_caracter(cadena:str, caracter:str) -> str:
#     palabras_con_caracter = []
#     palabras = cadena.split()

#     for palabra in palabras:
#         if caracter in palabra:
#             palabras_con_caracter.append(palabra)
    
#     return palabras_con_caracter
# lista_palabras = muestra_palabra_con_caracter("Hola mundo, me sacaron el stream", "o")
# print(lista_palabras)

# def conseguir_palabrs_segun_caracter(string:str, char:str) -> list:
#     lista_palabras = string.split()

#     return list(filter(lambda palabra: cantidad_caracteres in palabra, string.split(" ")))

#     #FORMA NO FILTER
#     #lista_palabras_segun_caracter = []

#     #for palabra in lista_palabras:
#         #if char in palabra:a
#             #lista_palabras_segun_caracter.append(palabra)
#     #return lista_palabras_segun_caracter


# # listar_palabras_con_caracter =\
# #     lambda string, caracter: list(filter(lambda palabra: char in palabra,))


# 7 - Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados

# def tomar_string_eliminar_espacios(texto:str) -> str:
#     return texto.strip()

# cadena = "    HOLA MUNDO    "
# resultado = tomar_string_eliminar_espacios(cadena)
# print(resultado)

# def eliminar_espacios_cadena(palabras:str) -> str:
#     palabra_sin_espacio = palabras.split()
#     palabra_sin_espacio = "".join(palabra_sin_espacio)
#     return palabra_sin_espacio

# print(eliminar_espacios_cadena("hola como estas capooo    "))

# def eliminar_espacios_cadena_2(palabras:str) -> str:
#     palabra_sin_espacio = palabras.replace(" ", "")
#     return palabra_sin_espacio

# print(eliminar_espacios_cadena("hola como estas capooo    "))



# 8 - Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario con el nombre y apellido, eliminando los espacios del comienzo y el final y colocando la primer letra en mayúscula
# def formatea_cadenas_en_diccionario(nombre: str, apellido: str) -> dict:
#     nombre_formateado = nombre.strip().capitalize()
#     apellido_formateado = apellido.strip().capitalize()

#     diccionario = {"nombre": nombre_formateado, "apellido": apellido_formateado}
#     return diccionario

# print(formatea_cadenas_en_diccionario("    nenu", "potenza      "))

# 9 - Escribir una función que tome una lista de nombres y los una en una sola cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".

# def formatea_lista_de_nombres_en_una_cadena(lista_de_nombres:list) -> str:
#     cadena_nombres = "\n"
#     cadena_nombres = cadena_nombres.join(lista_de_nombres)
#     return cadena_nombres

# formatea_lista_de_nombres_en_una_cadena(["Nenu", "Potenza", "Maga"])

# 10 - Escribir una función que tome un nombre y un apellido y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".
# Por ejemplo Facundo Falcone: f.falcone@utn-fra.com.ar

# def formatear_mail_inicial_apellido(nombre:str, apellido:str) -> str:
#     mail = f"{nombre[0].lower()}.{apellido.lower()}@utn-fra.com.ar"
#     return mail

# print(formatear_mail_inicial_apellido("Hernan", "Potenza"))

# 11 - Escribir una función que tome una lista de palabras y devuelva un string que contenga todas las palabras concatenadas con comas
# y "y" antes de la última palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el string resultante debería ser "manzanas, naranjas y bananas"..

# def concatenar_palabras_con_y_al_final(lista_de_palabras:list) -> str:
#     coma = ", "
#     nueva_lista_de_palabras = coma.join(lista_de_palabras)

#     largo_ultima_palabra = len(lista_de_palabras[-1])
#     final_primera_parte = (-largo_ultima_palabra)-2

#     primera_parte_cadena = nueva_lista_de_palabras[0:final_primera_parte]
#     segunda_parte_de_cadena = nueva_lista_de_palabras[final_primera_parte:]

#     segunda_parte_de_cadena = segunda_parte_de_cadena.replace(", ", " y ")

#     cadena_final = primera_parte_cadena + segunda_parte_de_cadena

#     return cadena_final

# 12 - concatenar_palabras_con_y_al_final(["Nenu", "Potenza", "Maga"])

# Escribir una función que tome un número de tarjeta de crédito como input, verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234". 

# Escribir una función que tome un correo electrónico y elimine cualquier carácter después del símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".

# Escribir una función que tome una URL y devuelva solo el nombre de dominio, por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..

# Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos, eliminando cualquier número o símbolo (sólo son válidos letras y espacios), por ejemplo: "H0l4, m4nd0!" -> "Hl mnd”

# Escribir una función que tome una cadena de texto y la convierta en un acrónimo, tomando la primera letra de cada palabra, por ejemplo: "Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.

# Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".


# Escribir una función que tome una cadena de caracteres y reemplace todas las letras mayúsculas por letras minúsculas y todas las letras minúsculas por letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"


# Escribir una función que tome una cadena de caracteres y cuente la cantidad de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.


# Escribir una función que tome una lista de direcciones de correo electrónico y las una en una sola cadena separada por punto y coma, por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".


# Crear una función que reciba como parámetro un string y devuelva un diccionario donde cada clave es una palabra y cada valor es un entero que indica cuántas veces aparece esa palabra dentro del string.

