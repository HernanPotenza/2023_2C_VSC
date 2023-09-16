
##################
# Hernan Potenza #
##################


'''
Crea un diccionario que represente los días de la semana, donde las claves son los nombres de los días y
los valores son los números correspondientes (por ejemplo, {"lunes": 1, "martes": 2, ...}). 
Imprime el valor correspondiente al día "miércoles".

'''
semana = {"lunes": 1, "martes": 2, "miercoles": 3, "jueves": 4, "viernes": 5, "sabado": 6, "domingo": 7}
print(f"Ejercicio 1: {semana['miercoles']}")


'''
Crea un diccionario que represente los meses del año, donde las claves son 
los nombres de los meses y los valores son sus números correspondientes (por ejemplo, {"enero": 1, "febrero": 2, ...}). 
Imprime el número correspondiente al mes "julio".
'''
mes = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6, "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12}
ejercicio_2 = mes.get("julio","no existe la clave")
print(f"Ejercicio 2: {ejercicio_2}") 


'''
Crea un diccionario que contenga la información de una película, como título, director y año de estreno. Luego, imprime el título de la película.
'''
pelicula = {"titulo": "Avatar","director": "el director de Avatar","Año de estreno": 1980}
ejercicio_3 = pelicula.get("titulo", "no existe la clave")
print(f"Ejercicio 3: Titulo de la pelicula: {ejercicio_3}")


'''
Crea un diccionario que contenga la información de una dirección: nombre de la calle, altura, localidad, 
código postal, partido y provincia. Luego, imprime el nombre de la calle, seguido de su altura.
'''
direccion = {"nombre_calle": "Oncativo", "altura": 473, "localidad": "Burzaco", "codigo_postal": 1852, "partido": "Almirante Brown", "provincia": "Buenos Aires"}
ejercicio_4_nombre_calle = direccion.get("nombre_calle", "no existe la clave")
ejercicio_4_altura = direccion.get("altura", "no exsite la clave")
print("Ejercicio 4: {0}, {1}".format(direccion.get("nombre_calle", "no existe la clave"), direccion.get("altura"))) 


'''
Crea un diccionario que represente los continentes, donde las claves son los nombres de los continentes y los 
valores son los números correspondientes (por ejemplo, {"América": 1, "Europa": 2, ...}). Imprime el valor correspondiente al continente "África".
'''
continentes = {"America": 1, "Europa": 2, "Africa": 3, "Asia": 4, "Oceania": 5, "Antartida": 6}
print("Ejercicio 5: {0}".format(continentes["Africa"]))


'''
Crea un diccionario que represente las estaciones del año, donde las claves son los nombres de las estaciones y los 
valores son los números correspondientes (por ejemplo, {"primavera": 1, "verano": 2, ...}). Imprime el valor correspondiente a la estación "invierno".
'''
estaciones_del_anio = {"primavera": 1, "verano": 2, "otonio": 3, "invierno": 4}
print("Ejercicio 6: {0}".format(estaciones_del_anio.get('invierno','le erraste a la clave')))


'''
Crea un diccionario que contenga la información de una canción: título, artista y duración. Luego, imprime la duración de la canción.
'''
cancion = {"titulo": "cancion x", "artista": "barack obama", "duracion": "17:51"}
print("Ejercicio 7: {0}".format(cancion.get('duracion', 'le erraste a la clave')))


'''
Crea un diccionario que represente las edades de varias personas, donde las claves son los nombres de las personas
y los valores son sus edades. Imprime la edad de la persona más joven.
'''
edades = {"Juan": 55, "Ana": 80, "Julia": 33, "Matias": 1}
valores = edades.values()
maximo = max(valores)
print("Ejercicio 8: {0}".format(maximo))


'''
Crea un diccionario que contenga las capitales de los países de América del Sur. 
Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.
'''
capitales = {"Argentina": "Buenos Aires", "Bolivia": "Sucre", "Brasil": "Brasilia", "Chile": "Santiago de Chile", "Colombia": "Bogotá", "Ecuador": "Quito", "Paraguay": "Asunción",
            "Peru": "Lima", "Surinam": "Parabarimo", "Trinidad y Tobago": "Puerto España", "Uruguay": "Montevideo", "Venezuela": "Caracas"}
pais = input("Ingrese nombre de pais para saber su capital: ").capitalize()
for paises in capitales:
    if paises == pais:
        print("Ejercicio 9: Pais: {0}, capital: {1}".format(pais, capitales.get(pais, 'le erraste a la clave')))

'''
Crea un diccionario que represente las notas de un examen de varios estudiantes, donde las claves son los nombres de los estudiantes y 
los valores son sus notas. Imprime el promedio de las notas.
'''
notas = {"Hernan": 10, "Tomas": 3, "Yanina": 9}
promedio = sum(notas.values()) / len(notas)
print("Ejercicio 10: {0}".format(promedio))