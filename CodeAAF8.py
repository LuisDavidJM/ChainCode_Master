# Función para calcular el valor de k
def find_k(f8_sequence, i):
    for k in range(i - 1, -1, -1):
        if f8_sequence[k] != f8_sequence[k + 1]:
            return k
    return len(f8_sequence) - 1

# Función para convertir de F8 a AAF8
def f8_to_aaf8(f8_sequence):
    n = len(f8_sequence)
    aaf8_sequence = [0] * n 

    for i in range(n):
        next_index = (i + 1) % n
        if f8_sequence[i] == f8_sequence[next_index]:
            aaf8_sequence[i] = 8
        else:
            k = find_k(f8_sequence, i)
            r = (f8_sequence[next_index] - f8_sequence[k]) % 8
            aaf8_sequence[i] = r

    return aaf8_sequence
