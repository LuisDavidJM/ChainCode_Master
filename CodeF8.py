import numpy as np

def calcular_direccion(delta_x, delta_y):
    """Calcula la dirección en el sistema F8 basado en la diferencia entre puntos."""
    norm = (delta_x**2 + delta_y**2)**0.5
    if norm == 0: return None  # Evita la división por cero
    # Normaliza la dirección
    delta_x, delta_y = delta_x / norm, delta_y / norm
    # Calcula el ángulo y ajusta el rango a [0, 2*pi)
    angulo = np.arctan2(delta_y, delta_x) % (2 * np.pi)
    
    # Divide el círculo en 8 sectores y asigna la dirección F8
    if angulo < np.pi / 8 or angulo >= 15 * np.pi / 8:
        return 0  # Derecha
    elif angulo < 3 * np.pi / 8:
        return 1  # Diagonal inferior derecha
    elif angulo < 5 * np.pi / 8:
        return 2  # Abajo
    elif angulo < 7 * np.pi / 8:
        return 3  # Diagonal inferior izquierda
    elif angulo < 9 * np.pi / 8:
        return 4  # Izquierda
    elif angulo < 11 * np.pi / 8:
        return 5  # Diagonal superior izquierda
    elif angulo < 13 * np.pi / 8:
        return 6 # Arriba
    else:
        return 7  # Diagonal superior derecha

def calcular_f8(contorno):
    """Calcula el código de cadena de Freeman de 8 direcciones para un contorno dado."""
    cadena_f8 = []
    
    # Asegura que el contorno sea cerrado conectando el último punto con el primero
    contorno_cerrado = np.vstack((contorno, [contorno[0]]))
    
    for i in range(len(contorno_cerrado) - 1):
        punto_actual = contorno_cerrado[i][0]
        punto_siguiente = contorno_cerrado[i + 1][0]
        
        delta_x = punto_siguiente[0] - punto_actual[0]
        delta_y = punto_siguiente[1] - punto_actual[1]
        
        direccion = calcular_direccion(delta_x, delta_y)
        if direccion is not None:
            cadena_f8.append(direccion)
    
    return cadena_f8


