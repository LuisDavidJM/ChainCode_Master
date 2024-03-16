from collections import Counter
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import CodeF8, CodeF4, CodeVCC

def encontrar_contorno(img):
    # Paso 1: Cargar la imagen
    imagen = cv2.imread(img)

    # Paso 2: Convertir a escala de grises y binarizar
    imagen_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _, imagen_binaria = cv2.threshold(imagen_grises, 127, 255, cv2.THRESH_BINARY)

    # Paso 3: Encontrar contornos
    contornos, _ = cv2.findContours(imagen_binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contornos = [contornos[1]]

    return contornos, imagen_grises

############################## CÓDIGO PRINCIPAL ####################################

img = 'Perro-128.png'
contornos, imagen_grises = encontrar_contorno(img)

punto_inicio = contornos[0][0]  # Accede al primer punto
print(f"Coordenada inicial: ({punto_inicio[0][0]}, {punto_inicio[0][1]})")

print("------------------------ Código F8 ------------------------")

# Lógica para procesar los contornos y generar vectores de Freeman
for contorno in contornos:
    codigo_f8 = CodeF8.calcular_f8(contorno)
# Convertir a cadena
cadena_f8_str = ''.join(str(digito) for digito in codigo_f8)
print(cadena_f8_str)

# Supongiendo que 'codigo_f8' es tu vector de Freeman para el contorno de interés
frecuencias = Counter(codigo_f8)
print("Frecuencia de aparición: ", end='')
for direccion, frecuencia in frecuencias.items():
    print(f"{direccion}:{frecuencia}", end=' ')

print("\n\n------------------------ Código F4 ------------------------")

# Convertir F8 a F4
codigo_f4 = CodeF4.f8_a_f4(codigo_f8, CodeF4.f8_f4)
print(codigo_f4)

# Supongiendo que 'codigo_f4' es tu vector de Freeman para el contorno de interés
frecuencias = Counter(codigo_f4)
print("Frecuencia de aparición: ", end='')
for direccion, frecuencia in frecuencias.items():
    print(f"{direccion}:{frecuencia}", end=' ')

print("\n\n------------------------ Código VCC ------------------------")

# Convertir y obtener la cadena VCC
cadena_vcc = CodeVCC.f4_to_vcc(codigo_f4, CodeVCC.f4_vcc)
# Convertir a cadena
cadena_vcc_str = ''.join(str(digito) for digito in cadena_vcc)
print(cadena_vcc_str)  # Imprimir la cadena VCC

# Supongiendo que 'codigo_vcc' es tu vector de Freeman para el contorno de interés
frecuencias = Counter(cadena_vcc)
print("Frecuencia de aparición: ", end='')
for direccion, frecuencia in frecuencias.items():
    print(f"{direccion}:{frecuencia}", end=' ')

############################## IMAGEN DE LOS CONTORNOS ####################################

# Forzar la descarga de la salida estándar
sys.stdout.flush()

# Visualizar los contornos encontrados
imagen_contornos = cv2.drawContours(np.zeros_like(imagen_grises), contornos, -1, (255, 255, 255), 1)
#plt.xticks(range(0,10,1))
#plt.yticks(range(0,10,1))
plt.imshow(imagen_contornos, cmap='gray')
plt.show()
