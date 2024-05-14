from collections import Counter
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import CodeF8, CodeF4, CodeVCC, CodeAF8, Code3OT, CodeAAF8

def encontrar_contorno(img):
    # Paso 1: Cargar la imagen
    imagen = cv2.imread(img)

    # Paso 2: Convertir a escala de grises y binarizar
    imagen_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _, imagen_binaria = cv2.threshold(imagen_grises, 127, 255, cv2.THRESH_BINARY)

    # Paso 3: Encontrar contornos
    contornos, _ = cv2.findContours(imagen_binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contornos_concatenados = [np.concatenate(contornos[1:])]

    return contornos_concatenados, contornos, imagen_grises

############################## CÓDIGO PRINCIPAL ####################################

img = 'PNG/Mujer.png'
contornos, contornos_img, imagen_grises = encontrar_contorno(img)

punto_inicio = contornos[0][0]  # Accede al primer punto
print(f"Coordenada inicial: ({punto_inicio[0][0]}, {punto_inicio[0][1]})")

print("------------------------ Código F8 ------------------------")

# Lógica para procesar los contornos y generar vectores de Freeman
for contorno in contornos:
    codigo_f8 = CodeF8.calcular_f8(contorno)
# Convertir a cadena
cadena_f8_str = ''.join(str(digito) for digito in codigo_f8)
print(cadena_f8_str)

# Inicializa las frecuencias para todos los símbolos posibles de F8 con cero
frecuencias_f8 = Counter({i: 0 for i in range(8)})
frecuencias_f8.update(codigo_f8)
print("Frecuencia de aparición: ", end='')
for direccion in range(8):
    print(f"{direccion}:{frecuencias_f8[direccion]}", end=' ')

print("\n\n------------------------ Código F4 ------------------------")

# Convertir F8 a F4
codigo_f4 = CodeF4.f8_a_f4(codigo_f8, CodeF4.f8_f4)
print(codigo_f4)

# Si cada símbolo es un carácter en la cadena, convierte la cadena en una lista de enteros
codigo_f4 = [int(simbolo) for simbolo in codigo_f4]

# Inicializa las frecuencias para todos los símbolos posibles de F4 con cero
frecuencias_f4 = Counter({i: 0 for i in range(4)})
frecuencias_f4.update(codigo_f4)
print("Frecuencia de aparición: ", end='')
for direccion in range(4):
    print(f"{direccion}:{frecuencias_f4[direccion]}", end=' ')

print("\n\n------------------------ Código VCC ------------------------")

# Convertir y obtener la cadena VCC
cadena_vcc = CodeVCC.f4_to_vcc(codigo_f4, CodeVCC.f4_vcc)
# Convertir a cadena
cadena_vcc_str = ''.join(str(digito) for digito in cadena_vcc)
print(cadena_vcc_str)  # Imprimir la cadena VCC

# Si cada símbolo es un carácter en la cadena, convierte la cadena en una lista de enteros
cadena_vcc = [int(simbolo) for simbolo in cadena_vcc]

# Inicializa las frecuencias para todos los símbolos posibles de VCC con cero
frecuencias_vcc = Counter({i: 0 for i in range(3)})
frecuencias_vcc.update(cadena_vcc)
print("Frecuencia de aparición: ", end='')
for direccion in range(3):
    print(f"{direccion}:{frecuencias_vcc[direccion]}", end=' ')

print("\n\n------------------------ Código AF8 ------------------------")

# Convertir y obtener la cadena AF8
cadena_af8 = CodeAF8.f8_to_af8(codigo_f8, CodeAF8.f8_af8)
# Convertir a cadena
cadena_af8_str = ''.join(str(digito) for digito in cadena_af8)
print(cadena_af8_str)  # Imprimir la cadena AF8

# Si cada símbolo es un carácter en la cadena, convierte la cadena en una lista de enteros
cadena_af8 = [int(simbolo) for simbolo in cadena_af8]

# Inicializa las frecuencias para todos los símbolos posibles de AF8 con cero
frecuencias_af8 = Counter({i: 0 for i in range(8)})
frecuencias_af8.update(cadena_af8)
print("Frecuencia de aparición: ", end='')
for direccion in range(8):
    print(f"{direccion}:{frecuencias_af8[direccion]}", end=' ')

print("\n\n------------------------ Código 3OT ------------------------")

# Convertir y obtener la cadena 3OT
cadena_3ot = Code3OT.f4_to_3ot(codigo_f4)
# Convertir a cadena
cadena_3ot_str = ''.join(str(digito) for digito in cadena_3ot)
print(cadena_3ot_str)  # Imprimir la cadena 3OT

# Si cada símbolo es un carácter en la cadena, convierte la cadena en una lista de enteros
cadena_3ot = [int(simbolo) for simbolo in cadena_3ot]

# Inicializa las frecuencias para todos los símbolos posibles de 3OT con cero
frecuencias_3ot = Counter({i: 0 for i in range(3)})
frecuencias_3ot.update(cadena_3ot)
print("Frecuencia de aparición: ", end='')
for direccion in range(3):
    print(f"{direccion}:{frecuencias_3ot[direccion]}", end=' ')

print("\n\n----------------------- Código AAF8 ------------------------")

c_f8 = [0,0,0,2,2,1,2,3,3,4,4,4,5,6,0,0,7,5,4,6,7]

# Calcular la secuencia AAF8
#cadena_aaf8 = CodeAAF8.f8_to_aaf8(c_f8)
cadena_aaf8 = CodeAAF8.f8_to_aaf8(codigo_f8)
# Convertir a cadena
cadena_3ot_str = ''.join(str(digito) for digito in cadena_aaf8)
print(cadena_3ot_str)

# Inicializa las frecuencias para todos los símbolos posibles de AAF8 con cero
frecuencias_aaf8 = Counter({i: 0 for i in range(9)})
frecuencias_aaf8.update(cadena_aaf8)
print("Frecuencia de aparición: ", end='')
for direccion in range(9):
    print(f"{direccion}:{frecuencias_aaf8[direccion]}", end=' ')

# Forzar la descarga de la salida estándar
sys.stdout.flush()

############################## IMAGEN DE LOS CONTORNOS ####################################

# Visualizar los contornos encontrados
imagen_contornos = cv2.drawContours(np.zeros_like(imagen_grises), contornos_img, -1, (255, 255, 255), 1)
plt.imshow(imagen_contornos, cmap='gray')

####################### HISTOGRAMAS DE FRECUANCIAS DE APARICIÓN #############################

# Inicializa una figura de matplotlib con subgráficos
fig, axs = plt.subplots(2, 3, figsize=(13, 7))  # 2 filas, 3 columnas de histogramas

# Diccionarios en una lista para iterar
frecuencias = [frecuencias_f4, frecuencias_f8, frecuencias_af8, frecuencias_aaf8, frecuencias_vcc, frecuencias_3ot]
titulos = ['F4', 'F8', 'AF8', 'AAF8', 'VCC', '3OT']

# Llenar cada subgráfico con los datos de frecuencia
for ax, freq, title in zip(axs.flat, frecuencias, titulos):
    # Datos para el histograma
    labels, values = zip(*sorted(freq.items()))
    
    # Crear el histograma
    ax.bar(labels, values)
    
    # Establecer título y etiquetas
    ax.set_title(f'Histograma de {title}')
    ax.set_xlabel('Símbolo')
    ax.set_ylabel('Frecuencia')
    ax.set_xticks(range(len(labels)))

# Ajustar layout para evitar la superposición
plt.tight_layout()

plt.show()
