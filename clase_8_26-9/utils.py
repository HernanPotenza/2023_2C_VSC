def formatear_puntaje(puntaje: str) -> str:
    puntaje_formateado = puntaje.zfill(4)
    return puntaje_formateado

def formatear_nombre_jugador(nombre: str) -> str:
    nombre_nuevo = nombre.strip().split(" ")
    nombre_formateado = nombre_nuevo[0].upper()
    return nombre_formateado