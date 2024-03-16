f8_f4 = [
    ["0", "010", "01", "0121", "*", "*", "*", "03"],
    [".", "10", "1", "121", "12", "*", "*", "3"],
    ["*", "10", "1", "121", "12", "1232", "*", "*"],
    ["*", "0", ".", "21", "2", "232", "23", "*"],
    ["*", "*", "*", "21", "2", "232", "23", "2303"],
    ["30", "*", "*", "1", ".", "32", "3", "303"],
    ["30", "2010", "*", "*", "*", "32", "3", "303"],
    ["0", "010", "01", "*", "*", "2", ".", "03"]
]

# Función para convertir F8 a F4 usando la matriz de transición
def f8_a_f4(f8_sequence, trans_matrix):
    f4_sequence = ""
    previous_f8 = 0  # Inicializamos la dirección anterior a 0 por defecto
    for current_f8 in f8_sequence:
        # Obtener el valor de transición basado en el vector anterior y actual F8
        transition_value = trans_matrix[previous_f8][current_f8]
        if transition_value not in [".", "*"]:  # Si no es un punto o un asterisco
            # Añadir el valor de transición a la secuencia F4 (considerando múltiples movimientos si es necesario)
            f4_sequence += transition_value
        previous_f8 = current_f8  # Actualizar la dirección anterior con la actual para la próxima iteración
    return f4_sequence