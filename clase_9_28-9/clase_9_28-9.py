import re
# textos = [
#     "NATHY PELUSO||BZRP Music Sessions#36",
#     "NATHY PELUSO||BZRP Music Sessions#37",
#     "NATHY PELUSO||BZRP Music Sessions%36",
#     "NATHY PELUSO||BZRP Music Sessions#3600000",
#     "NATHY PELUSO||BZRP Music Sessions#4",
#     "NATHY PELUSO||BZRP Music Sessions#"
# ]

# patron_de_busqueda = '^[a-zA-Z ]+\|\|[a-zA-Z ]+#[0-9]{1,2}$'
# nombre = ''

# # while not re.match(patron_de_busqueda, nombre):
# #     nombre = input('Escriba un nombrevalido de solo letras y espacios: ')

# # print(nombre)

# fechas = [
#     "2023/09/28 10:00:00 PM",
#     "2023/09/30 20:30:15",
#     "2023/09/28 10:00:00 AM",
#     "2023/09/30 99:90:99"
# ]

# patron_busqueda_fecha = '(^[0-9]{4}\/[0-9]{2}\/[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} (PM|AM)$)'
# patron_busqueda_fecha2 = '(^[0-9]{4}\/[0-9]{2}\/[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} [AMP]{2}$)'

# patron_fecha = '[0-9]{4}\/[0-9]{2}\/[0-9]{2}'
# patron_hora = '[0-9]{2}:[0-9]{2}:[0-9]{2}'
# patron_tiempo = '(PM|AM)'
# patron_completo = f'^{patron_fecha} {patron_hora} {patron_tiempo}$'
# patron = '[\s]{1}[^a-z]{1}[\s]{1}'
# for fecha in fechas:
#     if re.match(patron_completo, fecha):
#         print(fecha)

# # for texto in textos:
# #     if re.match(patron_de_busqueda, texto):
# #         print(texto)


texto = 'uno 13422 dos 2 tres 3 cuatro # cinco ! seis'

patron_busqueda = '[0-9]{1,2}'
busqueda = re.search(patron_busqueda, texto)
print(busqueda.group(0))

def buscar_receta(lista_recetas: list) -> None:
    patron = input('Ingrese la palabra a buscar para la receta: ')
    for receta in lista_recetas:
        hay_match = re.search(patron, receta["title"], re.IGNORECASE)
        if hay_match:
            print(receta["title"])

buscar_receta(lista_recetas_paulina)




normalizar datos stark 3 con regex