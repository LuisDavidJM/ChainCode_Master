import cv2
import numpy as np
from matplotlib import pyplot as plt

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
        return 7  # Diagonal inferior derecha
    elif angulo < 5 * np.pi / 8:
        return 6  # Abajo
    elif angulo < 7 * np.pi / 8:
        return 5  # Diagonal inferior izquierda
    elif angulo < 9 * np.pi / 8:
        return 4  # Izquierda
    elif angulo < 11 * np.pi / 8:
        return 3  # Diagonal superior izquierda
    elif angulo < 13 * np.pi / 8:
        return 2 # Arriba
    else:
        return 1  # Diagonal superior derecha

def calcular_vectores_freeman(contorno):
    """Calcula el código de cadena de Freeman de 8 direcciones para un contorno dado."""
    cadena_freeman = []
    
    # Asegura que el contorno sea cerrado conectando el último punto con el primero
    contorno_cerrado = np.vstack((contorno, [contorno[0]]))
    
    for i in range(len(contorno_cerrado) - 1):
        punto_actual = contorno_cerrado[i][0]
        punto_siguiente = contorno_cerrado[i + 1][0]
        
        delta_x = punto_siguiente[0] - punto_actual[0]
        delta_y = punto_siguiente[1] - punto_actual[1]
        
        direccion = calcular_direccion(delta_x, delta_y)
        if direccion is not None:
            cadena_freeman.append(direccion)
    
    return cadena_freeman

# Paso 1: Cargar la imagen
imagen = cv2.imread('Perro-256.png')

# Paso 2: Convertir a escala de grises y binarizar
imagen_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_, imagen_binaria = cv2.threshold(imagen_grises, 127, 255, cv2.THRESH_BINARY)

# Paso 3: Encontrar contornos
contornos, _ = cv2.findContours(imagen_binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contornos = [contornos[1]]

punto_inicio = contornos[0][0]  # Accede al primer punto
print(f"Coordenada de inicio del vector de Freeman: {punto_inicio}")

# Aquí podrías insertar la lógica para procesar los contornos y generar vectores de Freeman
for contorno in contornos:
    vectores_freeman = calcular_vectores_freeman(contorno)
    if vectores_freeman:  # Verifica si la lista no está vacía
        print("Código de cadena de Freeman:", vectores_freeman)
    else:
        print("No se pudo calcular el vector de Freeman para un contorno.")

# Visualizar los contornos encontrados (opcional)
imagen_contornos = cv2.drawContours(np.zeros_like(imagen_grises), contornos, -1, (255, 255, 255), 1)
#plt.xticks(range(0,10,1))
#plt.yticks(range(0,10,1))
plt.imshow(imagen_contornos, cmap='gray')
plt.show()
