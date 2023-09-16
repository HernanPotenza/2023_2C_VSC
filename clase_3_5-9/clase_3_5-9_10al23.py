
##################
# Hernan Potenza #
##################

ejercicios_a_corregir = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
opcion = int(input("Ingrese numero de ejercicio, del 10 al 23: "))
while opcion not in ejercicios_a_corregir:
    opcion = int(input("Ingrese numero de ejercicio, del 10 al 23 dije: "))

match(opcion):
    case 10:
        '''
        Crea un diccionario que represente las notas de un examen de varios estudiantes, donde las claves son los nombres de los estudiantes y 
        los valores son sus notas. Imprime el promedio de las notas.
        '''
        notas = {"Hernan": 10, "Tomas": 3, "Yanina": 9}
        promedio = sum(notas.values()) / len(notas)
        print("Ejercicio 10: {0}".format(promedio))

    case 11:
        '''
        Crea un diccionario que represente una lista de tareas por hacer. Cada clave del diccionario debe ser el nombre de una tarea y 
        cada valor debe ser su estado (los estados son:  pendiente, en proceso, completada). Imprimir todas las tareas seguido de su estado
        '''
        tareas = {"estudiar": "pendiente", "hacer_tarea": "en proceso", "cenar": "pendiente", "cursar_martes": "completada"}
        print("Ejercicio 11:")
        for tarea in tareas:
            print("{0}: {1}".format(tarea, tareas.get(tarea, 'le erraste a la clave')))
    case 12:
        '''
        Crea un diccionario que represente una lista de las compras. Cada clave del diccionario debe ser el nombre de un producto y 
        cada valor debe ser su cantidad. Pedir al usuario que ingrese el nombre del producto e imprimir la cantidad
        '''
        lista_de_compras = {"milanesas": 5, "agua": 3, "vasos": 10, "sal": 1}
        entrada = input("Ingrese producto: ").lower()
        print("Ejercicio 12: {0}".format(lista_de_compras.get(entrada)))

    case 13:
        '''
        Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa. Luego, pedirle al 
        usuario un nivel de dificultad, buscar los que coinciden e imprimir sus nombres
        '''
        juegos_de_mesa = {"ajedrez": 7, "damas": 3, "ludo": 3, "generala": 7, "uno": 3}
        flag = 0
        print(juegos_de_mesa)
        entrada = int(input("Ingrese dificultad: "))
        for juego in juegos_de_mesa:
            if juegos_de_mesa[juego] == entrada:
                if flag == 0:
                    flag = 1
                    print("Ejercicio 13: ")
                print("{0}".format(juego))

    case 14:
        '''
        Crea un diccionario que contenga el nombre como clave y el puntaje como valor de varios jugadores en un juego. 
        Luego, pedirle al usuario el nombre del jugador y nuevo puntaje y actualizar el valor correspondiente en el diccionario.
        '''
        puntajes = {"Juan": 3, "Marcos": 5, "Hernan": 8, "Emiliano": 10}
        print(puntajes)  
        entrada = input("Ingrese nombre del jugador: ").capitalize()
        for jugador in puntajes:
            if jugador == entrada:
                nuevo_puntaje = int(input("Ingrese nuevo puntaje: "))
                puntajes[jugador] = nuevo_puntaje
        print("Ejercicio 14: {0}".format(puntajes))

    case 15:
        '''
        Crea un diccionario que contenga el nombre y el sueldo de varios empleados. Luego, permite al usuario aumentar el sueldo de 
        un empleado y actualizar el valor correspondiente en el diccionario.
        '''
        sueldos = {"Marcos": 180000, "Juan": 5}
        print(sueldos)  
        entrada = input("Ingrese nombre del empleado para aumentarle el sueldo: ").capitalize()
        for empleado in sueldos:
            if empleado == entrada:
                nuevo_sueldo = int(input("Ingrese nuevo sueldo: "))
                sueldos[empleado] = nuevo_sueldo
        print("Ejercicio 15: {0}".format(sueldos))


    case 16:
        '''
        Crea un diccionario que represente una lista de tareas pendientes, donde las claves son las tareas y los valores son "True" si están completadas 
        y "False" si no lo están. Solicita al usuario el nombre de una tarea y modifica el valor para marcarla como completada. Imprimir el listado de tareas pendientes

        '''
        tareas_pendientes = {"Estudiar": True, "Dormir": False, "Repasar": True,  "Comer": False,  "Aprobar": False}
        print(tareas_pendientes)
        entrada = input("Ingrese tarea a modificar: ").capitalize()
        for tarea in tareas_pendientes:
            if tarea == entrada:
                tareas_pendientes[tarea] = True

        for tarea in tareas_pendientes:
            if tareas_pendientes[tarea] == False:
                print("Ejercicio 16: Tareas pendientes: {0}".format(tarea))

    case 17:
        '''
        Crea un diccionario que represente las películas de un cine, donde las claves son los nombres de las películas 
        y los valores son los horarios correspondientes. Modifica el horario de la película "Avengers: Endgame" a las 19:30.
        '''
        peliculas = {"Avengers: Endgame": "22:30", "Ironman": "15:00", "Thor": "08:00"}
        print(peliculas)
        peliculas["Avengers: Endgame"] = "19:30"
        print("Ejercicio 17: Despues de modificar endgame a las 19:30: \n{0}".format(peliculas))

    case 18:
        '''
        Crea un diccionario que represente los juegos de una consola, donde las claves son los nombres de 
        los juegos y los valores son las puntuaciones correspondientes. Solicita al usuario el nombre de 
        un juego y luego su puntuación, si el juego no existe agregarlo y si existe actualizar su puntuación 
        '''
        juegos = {"flatout 2": 9, "prototype": 9, "gta san andreas": 10, "mario bros": 2}
        flag = 0
        print(juegos)
        entrada = input("Ingrese nombre de juego, todo en minusculas: ")
        for juego in juegos:
            if juego == entrada:
                nuevo_puntaje = int(input("Ingrese puntuacion: "))
                juegos[juego] = (nuevo_puntaje)
                flag = 1
        if flag == 0:
            juegos[entrada] = int(input("Ingrese puntuacion: "))
        print("Ejercicio 18: {0}".format(juegos))

    case 19:
        '''
        Crea un diccionario que represente las temperaturas de una ciudad durante una semana, donde las claves son los días de la semana y 
        los valores son las temperaturas correspondientes. Calcula la temperatura promedio de la semana.
        '''
        semana = {"lunes": 22, "martes": 19, "miercoles": 15, "jueves": 10, "viernes": 12, "sabado": 15, "domingo": 10}
        print(semana)
        promedio =  sum(semana.values()) / len(semana)
        print("Ejercicio 19: promedio de temperatura de la semana: {0}".format(promedio))

    case 20:
        '''
        Crea un diccionario que represente los asientos de un avión, donde las claves son los números de asientos y 
        los valores son "True" si están ocupados y "False" si no lo están. Solicita al usuario un número de asiento 
        y modifica su valor para marcarlo como ocupado. Luego imprimí la lista de asientos libres
        '''
        asientos_de_avion = {"1": True, "2": False, "3": False, "4": True, "5": False, "6": False, "7": False, "8": True}
        flag = 0
        print(asientos_de_avion)
        entrada = input("Ingrese numero de asiento: ")
        for asiento in asientos_de_avion:
            if asiento == entrada:
                asientos_de_avion[asiento] = True

        for asiento in asientos_de_avion:
            if asientos_de_avion[asiento] == False:
                if flag == 0:
                    flag = 1
                    print("Ejercicio 20: Asientos libres: ")
                print("{0}".format(asiento))

    case 21:        
        '''
        Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las categorías 
        y los valores son los gastos correspondientes. Calcula el total de gastos de la persona.
        '''
        gastos = {"Comida": 15000, "Facultad": 10000, "Gato": 3000, "Bebida": 12000, "Otros": 20000}
        print("Ejercicio 21: Total de gastos: {0}".format(sum(gastos.values())))

    case 22:
        '''
        Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las categorías 
        y los valores son los gastos correspondientes. Calcula el total de gastos de la persona en el mes.
        '''
        gastos = {"Comida": 15000, "Facultad": 10000, "Gato": 3000, "Bebida": 12000, "Otros": 20000}
        print("Ejercicio 22: Total de gastos: {0}".format(sum(gastos.values())))

    case 23:
        '''
        Crea un diccionario que represente los contactos de un teléfono, donde las claves son los nombres de las personas y 
        los valores son los números de teléfono correspondientes. Solicitar al usuario el nombre de un contacto: agregarlo 
        al diccionario en caso de que no exista. En caso de que exista modificar el número de teléfono del contacto.
        '''
        contactos_telefono = {"Marcos": 42381919, "Hernan": 42992588, "Juan": 43341122}
        flag = 0
        print(contactos_telefono)
        entrada = input("Ingrese nombre para modificar el telefono: ").capitalize()
        for contacto in contactos_telefono:
            if contacto == entrada:
                nuevo_telefono = int(input("Ingrese nuevo telefono: "))
                contactos_telefono[contacto] = nuevo_telefono
                flag = 1
        if flag == 0:
            contactos_telefono[entrada] = int(input("Ingrese telefono para el nuevo contacto: "))
        print("Ejercicio 23: {0}".format(contactos_telefono))





















