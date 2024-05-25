import numpy as np

def calculate_entropy(histogram):
    total_count = sum(histogram.values())
    entropy = 0
    for count in histogram.values():
        if count > 0:
            probability = count / total_count
            entropy -= probability * np.log2(probability)
    return entropy
