f8_af8 = [
    ["0", "1", "2", "3", "4", "5", "6", "7"],
    ["7", "0", "1", "2", "3", "4", "5", "6"],
    ["6", "7", "0", "1", "2", "3", "4", "5"],
    ["5", "6", "7", "0", "1", "2", "3", "4"],
    ["4", "5", "6", "7", "0", "1", "2", "3"],
    ["3", "4", "5", "6", "7", "0", "1", "2"],
    ["2", "3", "4", "5", "6", "7", "0", "1"],
    ["1", "2", "3", "4", "5", "6", "7", "0"]
]

# Convertir de F8 a AF8
def f8_to_af8(f8_sequence, trans_matrix):
    af8_sequence = []
    # La dirección inicial (para i-1 cuando i es el primer elemento) es la última dirección de la secuencia,
    # ya que estamos asumiendo un contorno cerrado
    prev_dir = f8_sequence[-1]

    for i in range(len(f8_sequence)):
        current_dir = f8_sequence[i]
        # La transición se encuentra en la columna 'current_dir' y la fila 'prev_dir'
        af8_dir = trans_matrix[prev_dir][current_dir]
        af8_sequence.append(af8_dir)
        prev_dir = current_dir  # Actualizamos prev_dir para la próxima iteración

    return af8_sequence