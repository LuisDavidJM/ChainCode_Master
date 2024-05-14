# Función para convertir de F4 a 3OT
def f4_to_3ot(f4_sequence):
    _3ot_sequence = []
    n = len(f4_sequence)

    for i in range(n):
        # El elemento siguiente en la secuencia cíclica
        next_i = (i + 1) % n
        
        # Si C_F4(i + 1) es igual a C_F4(i), entonces C_3OT(i) es 0
        if f4_sequence[next_i] == f4_sequence[i]:
            _3ot_sequence.append("0")
        else:
            # Si no son iguales, verificamos las condiciones para 1 y 2
            k = find_k(f4_sequence, i)
            if f4_sequence[next_i] == f4_sequence[k]:
                _3ot_sequence.append("1")
            elif f4_sequence[next_i] == (f4_sequence[k] + 2) % 4:
                _3ot_sequence.append("2")
            else:
                # Este caso no debería ocurrir con una secuencia F4 válida
                pass

    return _3ot_sequence

# Función para encontrar el índice k como se describe en la imagen
def find_k(f4_sequence, i):
    # Encontrar k tal que C_F4(k) != C_F4(k+1) == C_F4(k+2) ... == C_F4(i)
    k = (i - 1) % len(f4_sequence)
    while f4_sequence[k] == f4_sequence[i] and k != i:
        k = (k - 1) % len(f4_sequence)
    return k