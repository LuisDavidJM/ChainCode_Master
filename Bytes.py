import heapq
from collections import defaultdict
import matplotlib.pyplot as plt
import Cadenas

class HuffmanNode:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(frequencies):
    heap = [HuffmanNode(symbol, freq) for symbol, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(frequency=node1.frequency + node2.frequency)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_huffman_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.symbol is not None:
            codebook[node.symbol] = prefix
        generate_huffman_codes(node.left, prefix + "0", codebook)
        generate_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

def calculate_huffman_encoded_size(frequencies, huffman_codes):
    total_bits = 0
    for symbol, freq in frequencies.items():
        total_bits += freq * len(huffman_codes[symbol])
    total_bytes = total_bits / 8
    return total_bits, total_bytes

# Diccionario de imágenes predefinidas
image_paths = {
    'Elefante': 'PNG/Elefante-1024.png',
    'Bigote': 'PNG/Bigote-64.png',
    'Lentes': 'PNG/Lentes-64.png',
    'Mancha': 'PNG/Mancha-64.png',
    'Mujer': 'PNG/Mujer.png',
    'Perro': 'PNG/Perro-64.png',
    'Pinguino': 'PNG/Pinguino-1024.png',
    'Puerco': 'PNG/Puerco-1024.png',
    'Tigre': 'PNG/Tigre-1024.png'
}

names = ['CÓDIGO F4', 'CÓDIGO F8', 'CÓDIGO AF8', 'CÓDIGO AAF8', 'CÓDIGO VCC', 'CÓDIGO 3OT']

# Inicializar acumuladores para las sumas de bytes de cada tipo de código de cadena
total_bytes_per_code = defaultdict(float)
code_counts = defaultdict(int)

for image_name, image_path in image_paths.items():
    contornos, _, _ = Cadenas.encontrar_contorno(image_path)
    _, frequencies_array = Cadenas.codigos(contornos)

    for i, frequencies in enumerate(frequencies_array):
        name = names[i]

        # Construir el árbol de Huffman
        huffman_tree = build_huffman_tree(frequencies)

        # Generar los códigos de Huffman para cada símbolo
        huffman_codes = generate_huffman_codes(huffman_tree)

        # Calcular el tamaño total en bits y bytes de la cadena codificada
        total_bits, total_bytes = calculate_huffman_encoded_size(frequencies, huffman_codes)

        # Acumular los bytes para el cálculo del promedio
        total_bytes_per_code[name] += total_bytes
        code_counts[name] += 1

        # Imprimir tabla de valores
        print(f"\n{name} - {image_name}")
        print(f"{'Símbolo':<10} {'Frecuencia':<10} {'Código Huffman':<15} {'Bits':<10}")
        print("="*50)

        for symbol in frequencies:
            freq = frequencies[symbol]
            huffman_code = huffman_codes[symbol]
            symbol_bits = freq * len(huffman_code)
            print(f"{symbol:<10} {freq:<10} {huffman_code:<15} {symbol_bits:<10}")

        # Imprimir la cantidad total de bits y bytes
        print("="*50)
        print(f"{'Total en bits':<35} {total_bits:.2f} bits")
        print(f"{'Total en bytes':<35} {total_bytes:.2f} bytes")

# Calcular y imprimir los promedios de bytes para cada tipo de código de cadena
print("\nPromedio de bytes por código de cadena:")
print("="*50)
for name in names:
    average_bytes = total_bytes_per_code[name] / code_counts[name]
    print(f"{name:<35} {average_bytes:.2f} bytes")

# Calcular y graficar el histograma de promedios de bytes por código de cadena
averages = [total_bytes_per_code[name] / code_counts[name] for name in names]

plt.figure(figsize=(10, 6))
plt.bar(names, averages, color='skyblue')
plt.xlabel('Código de Cadena')
plt.ylabel('Promedio de Bytes')
plt.title('Promedio de Bytes por Código de Cadena')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
