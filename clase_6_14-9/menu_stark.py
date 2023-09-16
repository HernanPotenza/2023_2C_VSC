
##################
# Hernan Potenza #
##################


from biblioteca_funciones_stark import *
from data_stark import lista_personajes




def menu_stark() -> None:
    '''
    Es la funcion principal que corre el menu y llama a todas las funciones que sean necesarias
    Recibe: nada
    Devuelve: nada
    '''
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
    
    ejercicios_a_corregir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    continuar = None

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

                    case 9:                    
                        mensaje = "Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)"                    
                        print(f"Su eleccion fue I: {mensaje}")
                        mensaje_final = f"Superheroe M mas alto: {buscar_superheroe_mas_alto_bajo_por_genero(lista_personajes, 'M')['nombre']}\n\
Superheroe F mas alta: {buscar_superheroe_mas_alto_bajo_por_genero(lista_personajes, 'F')['nombre']}\n\
Superheroe M mas bajo: {buscar_superheroe_mas_alto_bajo_por_genero(lista_personajes, 'M', False)['nombre']}\n\
Superheroe F mas baja: {buscar_superheroe_mas_alto_bajo_por_genero(lista_personajes, 'F', False)['nombre']}"
                        print(mensaje_final)

                    case 10:
                        mensaje = "Determinar cuántos superhéroes tienen cada tipo de color de ojos"                    
                        print(f"Su eleccion fue J: {mensaje}")
                        cantidad_superheroes_por_color_ojos = devuelve_cantidad_superheroe_por_color_ojos(lista_personajes)
                        print(f"Cantidad de supereroes por color de ojos: {cantidad_superheroes_por_color_ojos}")

                    case 11:                    
                        mensaje = "Determinar cuántos superhéroes tienen cada tipo de color de pelo"                    
                        print(f"Su eleccion fue K: {mensaje}")
                        cantidad_superheroes_por_color_pelo = devuelve_cantidad_superheroe_por_color_pelo(lista_personajes)
                        print(f"Cantidad de supereroes por color de pelo: {cantidad_superheroes_por_color_pelo}")

                    case 12:
                        mensaje = "Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’)"                    
                        print(f"Su eleccion fue L: {mensaje}")
                        cantidad_superheroes_por_inteligencia = devuelve_cantidad_superheroe_por_inteligencia(lista_personajes)
                        print(f"Cantidad de supereroes por inteligencia: {cantidad_superheroes_por_inteligencia}")

                    case 13:
                        mensaje = "Listar todos los superhéroes agrupados por color de ojos"                    
                        print(f"Su eleccion fue M: {mensaje}")
                        listar_cantidad_superheroe_por_color_ojos(lista_personajes)

                    case 14:
                        mensaje = "Listar todos los superhéroes agrupados por color de pelo"                    
                        print(f"Su eleccion fue N: {mensaje}")
                        listar_cantidad_superheroe_por_color_ojos(lista_personajes)

                    case 15:
                        mensaje = "Listar todos los superhéroes agrupados por tipo de inteligencia"                    
                        print(f"Su eleccion fue O: {mensaje}")
                        listar_cantidad_superheroe_por_tipo_inteligencia(lista_personajes)

                    case 16:
                        break