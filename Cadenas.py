from collections import Counter
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import CodeF8, CodeF4, CodeVCC, CodeAF8, Code3OT, CodeAAF8

def encontrar_contorno(img):
    # Cargar la imagen
    imagen = cv2.imread(img)

    # Convertir a escala de grises y binarizar
    imagen_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _, imagen_binaria = cv2.threshold(imagen_grises, 127, 255, cv2.THRESH_BINARY)

    # Encontrar contornos
    contornos, _ = cv2.findContours(imagen_binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contornos_concatenados = [np.concatenate(contornos[1:])]

    return contornos_concatenados, contornos, imagen_grises

def codigos(contornos):

    #print("------------------------ Código F8 ------------------------")
    for contorno in contornos:
        codigo_f8 = CodeF8.calcular_f8(contorno)
    cadena_f8_str = ''.join(str(digito) for digito in codigo_f8)
    frecuencias_f8 = Counter({i: 0 for i in range(8)})
    frecuencias_f8.update(codigo_f8)

    #print("\n\n------------------------ Código F4 ------------------------")
    codigo_f4 = CodeF4.f8_a_f4(codigo_f8, CodeF4.f8_f4)
    codigo_f4_str = codigo_f4
    codigo_f4 = [int(simbolo) for simbolo in codigo_f4]
    frecuencias_f4 = Counter({i: 0 for i in range(4)})
    frecuencias_f4.update(codigo_f4)

    #print("\n\n------------------------ Código VCC ------------------------")
    cadena_vcc = CodeVCC.f4_to_vcc(codigo_f4, CodeVCC.f4_vcc)
    cadena_vcc_str = ''.join(str(digito) for digito in cadena_vcc)
    cadena_vcc = [int(simbolo) for simbolo in cadena_vcc]
    frecuencias_vcc = Counter({i: 0 for i in range(3)})
    frecuencias_vcc.update(cadena_vcc)

    #print("\n\n------------------------ Código AF8 ------------------------")
    cadena_af8 = CodeAF8.f8_to_af8(codigo_f8, CodeAF8.f8_af8)
    cadena_af8_str = ''.join(str(digito) for digito in cadena_af8)
    cadena_af8 = [int(simbolo) for simbolo in cadena_af8]
    frecuencias_af8 = Counter({i: 0 for i in range(8)})
    frecuencias_af8.update(cadena_af8)

    #print("\n\n------------------------ Código 3OT ------------------------")
    cadena_3ot = Code3OT.f4_to_3ot(codigo_f4)
    cadena_3ot_str = ''.join(str(digito) for digito in cadena_3ot)
    cadena_3ot = [int(simbolo) for simbolo in cadena_3ot]
    frecuencias_3ot = Counter({i: 0 for i in range(3)})
    frecuencias_3ot.update(cadena_3ot)

    #print("\n\n----------------------- Código AAF8 ------------------------")
    cadena_aaf8 = CodeAAF8.f8_to_aaf8(codigo_f8)
    cadena_aaf8_str = ''.join(str(digito) for digito in cadena_aaf8)
    frecuencias_aaf8 = Counter({i: 0 for i in range(9)})
    frecuencias_aaf8.update(cadena_aaf8)

    codigos_cadena = [codigo_f4_str, cadena_f8_str, cadena_af8_str, cadena_aaf8_str, cadena_vcc_str, cadena_3ot_str]
    frecuencias_cadenas = [frecuencias_f4, frecuencias_f8, frecuencias_af8, frecuencias_aaf8, frecuencias_vcc, frecuencias_3ot]

    return codigos_cadena, frecuencias_cadenas