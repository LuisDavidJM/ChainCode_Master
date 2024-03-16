f4_vcc = [
    ["0", "1", "*", "2"],
    ["2", "0", "1", "*"],
    ["*", "2", "0", "1"],
    ["1", "*", "2", "0"]
]

# Función para convertir de F4 a VCC
def f4_to_vcc(f4_sequence, trans_matrix):
    vcc_sequence = []
    
    for i in range(1, len(f4_sequence)):
        current = int(f4_sequence[i])
        previous = int(f4_sequence[i - 1])
        vcc_symbol = trans_matrix[previous][current]
        if vcc_symbol != '*':
            vcc_sequence.append(vcc_symbol)
    
    return vcc_sequence