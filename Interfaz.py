from collections import Counter
import sys
import cv2
import numpy as np
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QPushButton, QWidget, QTextEdit
from PyQt5.QtWidgets import QSplitter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import Cadenas
import Entropy

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class ImageSelector(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Códigos de Cadena')
        self.setWindowIcon(QIcon('icon.png'))

        # Diccionario de imágenes predefinidas
        self.image_paths = {
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

        self.central_widget = QWidget()
        self.central_widget.setStyleSheet("background-color: lightblue;")
        self.setCentralWidget(self.central_widget)

        self.resize(2300, 1500)

        self.splitter = QSplitter(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.addWidget(self.splitter)

        # Layout vertical para los botones
        self.button_widget = QWidget()
        self.button_layout = QVBoxLayout(self.button_widget)
        self.splitter.addWidget(self.button_widget)

        # Layout vertical para la información
        self.info_widget = QWidget()
        self.info_layout = QVBoxLayout(self.info_widget)
        self.splitter.addWidget(self.info_widget)

        self.select_image_label = QLabel('Selecciona la imagen')
        self.select_image_label.setStyleSheet("font-size: 25px;")
        self.button_layout.addWidget(self.select_image_label)

        self.image_combo = QComboBox()
        self.image_combo.addItems(self.image_paths.keys())
        self.image_combo.setStyleSheet("font-size: 25px; background-color: white;")
        self.button_layout.addWidget(self.image_combo)

        self.image_label = QLabel()
        self.info_layout.addWidget(self.image_label)

        # Botones para seleccionar códigos de cadena
        self.f4_button = QPushButton('F4')
        self.f8_button = QPushButton('F8')
        self.af8_button = QPushButton('AF8')
        self.aaf8_button = QPushButton('AAF8')
        self.vcc_button = QPushButton('VCC')
        self.ot_button = QPushButton('3OT')

        self.f4_button.setStyleSheet("""
            QPushButton {
                background-color: white;
            }
            QPushButton:hover {
                background-color: lightgray;
            }
        """)
        self.f8_button.setStyleSheet("""
            QPushButton {
                background-color: white;
            }
            QPushButton:hover {
                background-color: lightgray;
            }
        """)
        self.af8_button.setStyleSheet("""
            QPushButton {
                background-color: white;
            }
            QPushButton:hover {
                background-color: lightgray;
            }
        """)
        self.aaf8_button.setStyleSheet("""
            QPushButton {
                background-color: white;
            }
            QPushButton:hover {
                background-color: lightgray;
            }
        """)
        self.vcc_button.setStyleSheet("""
            QPushButton {
                background-color: white;
            }
            QPushButton:hover {
                background-color: lightgray;
            }
        """)
        self.ot_button.setStyleSheet("""
            QPushButton {
                background-color: white;
            }
            QPushButton:hover {
                background-color: lightgray;
            }
        """)

        self.select_code_label = QLabel('Selecciona el código de cadena')
        self.select_code_label.setStyleSheet("font-size: 25px;")
        self.button_layout.addWidget(self.select_code_label)

        self.button_layout.addWidget(self.f4_button)
        self.button_layout.addWidget(self.f8_button)
        self.button_layout.addWidget(self.af8_button)
        self.button_layout.addWidget(self.aaf8_button)
        self.button_layout.addWidget(self.vcc_button)
        self.button_layout.addWidget(self.ot_button)

        self.clear_button = QPushButton('Limpiar')
        self.clear_button.setStyleSheet("""
            QPushButton {
                background-color: yellow;
            }
            QPushButton:hover {
                background-color: green;
            }
        """)
        self.button_layout.addWidget(self.clear_button)

        self.entropy_label = QLabel('Entropía')
        self.entropy_label.setStyleSheet("font-size: 25px;")
        self.button_layout.addWidget(self.entropy_label)

        self.code_label = QLabel('Codigo de cadena')
        self.code_label.setStyleSheet("font-size: 25px;")
        self.button_layout.addWidget(self.code_label)

        # TextEdit para mostrar el código de cadena
        self.text_edit = QTextEdit()
        self.text_edit.setMinimumWidth(800) 
        self.text_edit.setStyleSheet("background-color: white;")
        self.button_layout.addWidget(self.text_edit)

        self.total_entropy_label = QLabel('Entropías Totales')
        self.total_entropy_label.setStyleSheet("font-size: 25px;")
        self.button_layout.addWidget(self.total_entropy_label)

        # Canvas para Matplotlib para mostrar imagen e histograma
        self.canvas_image = MplCanvas(self, width=5, height=5, dpi=200)
        self.info_layout.addWidget(self.canvas_image)

        self.canvas_histogram = MplCanvas(self, width=5, height=5, dpi=200)
        self.info_layout.addWidget(self.canvas_histogram)

        # Conectar selección de imagen y botones a funciones
        self.image_combo.currentIndexChanged.connect(self.display_image)
        self.f4_button.clicked.connect(lambda: self.display_histogram_and_code(0, 'F4'))
        self.f8_button.clicked.connect(lambda: self.display_histogram_and_code(1, 'F8'))
        self.af8_button.clicked.connect(lambda: self.display_histogram_and_code(2, 'AF8'))
        self.aaf8_button.clicked.connect(lambda: self.display_histogram_and_code(3, 'AAF8'))
        self.vcc_button.clicked.connect(lambda: self.display_histogram_and_code(4, 'VCC'))
        self.ot_button.clicked.connect(lambda: self.display_histogram_and_code(5, '3OT'))
        self.clear_button.clicked.connect(self.clear_content)

        self.selected_image = None
        self.contornos = None
        self.contornos_img = None
        self.imagen_grises = None
        self.codigos_cadena = None
        self.frecuencias_cadenas = None

        # Mostrar la imagen seleccionada al inicio
        self.display_image()

        self.calculate_total_entropy()

    def clear_content(self):
        self.image_label.clear()
        self.canvas_image.axes.clear()
        self.canvas_image.draw()
        
        self.canvas_histogram.axes.clear()
        self.canvas_histogram.draw()
        
        self.text_edit.clear()
        self.entropy_label.clear()


    def display_image(self):
        self.clear_content() 
        selected_key = self.image_combo.currentText()
        image_path = self.image_paths[selected_key]

        # Encontrar contornos y calcular códigos de cadena
        self.contornos, self.contornos_img, self.imagen_grises = Cadenas.encontrar_contorno(image_path)
        self.codigos_cadena, self.frecuencias_cadenas = Cadenas.codigos(self.contornos)

        # Mostrar la imagen de los contornos usando Matplotlib
        imagen_contornos = cv2.drawContours(np.zeros_like(self.imagen_grises), self.contornos_img, -1, (255, 255, 255), 1)
        
        self.canvas_image.axes.clear()
        self.canvas_image.axes.imshow(imagen_contornos, cmap='gray')
        self.canvas_image.draw()

    def display_histogram_and_code(self, index, title):
        self.canvas_histogram.axes.clear()

        # Obtener el código de cadena y las frecuencias correspondientes
        cadena = self.codigos_cadena[index]
        frecuencias = self.frecuencias_cadenas[index]

        # Calcular la entropía
        entropy = Entropy.calculate_entropy(frecuencias)

        # Crear el histograma
        labels, values = zip(*sorted(frecuencias.items()))
        self.canvas_histogram.axes.bar(labels, values)
        self.canvas_histogram.axes.set_title(f'Histograma de {title}')
        self.canvas_histogram.axes.set_xlabel('Símbolo')
        self.canvas_histogram.axes.set_ylabel('Frecuencia')
        self.canvas_histogram.axes.set_xticks(range(len(labels)))

        # Mostrar el código de cadena en el QTextEdit
        self.text_edit.setText(str(cadena))

        # Mostrar la entropía en el QLabel
        self.entropy_label.setText(f'Entropía: {entropy:.4f}')

        self.canvas_histogram.draw()

    def calculate_total_entropy(self):
        total_frequencies_F4 = Counter()
        total_frequencies_F8 = Counter()
        total_frequencies_AF8 = Counter()
        total_frequencies_AAF8 = Counter()
        total_frequencies_VCC = Counter()
        total_frequencies_3OT = Counter()
        
        for image_key in self.image_paths.keys():
            image_path = self.image_paths[image_key]
            contornos, contornos_img, imagen_grises = Cadenas.encontrar_contorno(image_path)
            codigos_cadena, frecuencias_cadenas = Cadenas.codigos(contornos)
            
            total_frequencies_F4.update(frecuencias_cadenas[0])
            total_frequencies_F8.update(frecuencias_cadenas[1])
            total_frequencies_AF8.update(frecuencias_cadenas[2])
            total_frequencies_AAF8.update(frecuencias_cadenas[3])
            total_frequencies_VCC.update(frecuencias_cadenas[4])
            total_frequencies_3OT.update(frecuencias_cadenas[5])
        
        # Calcular la entropía total para cada tipo de código de cadena
        total_entropy_F4 = Entropy.calculate_entropy(total_frequencies_F4)
        total_entropy_F8 = Entropy.calculate_entropy(total_frequencies_F8)
        total_entropy_AF8 = Entropy.calculate_entropy(total_frequencies_AF8)
        total_entropy_AAF8 = Entropy.calculate_entropy(total_frequencies_AAF8)
        total_entropy_VCC = Entropy.calculate_entropy(total_frequencies_VCC)
        total_entropy_3OT = Entropy.calculate_entropy(total_frequencies_3OT)
        
        # Actualizar el QLabel con todas las entropías
        entropies_text = (
            f'Entropía promedio F4: {total_entropy_F4:.4f}\n'
            f'Entropía promedio F8: {total_entropy_F8:.4f}\n'
            f'Entropía promedio AF8: {total_entropy_AF8:.4f}\n'
            f'Entropía promedio AAF8: {total_entropy_AAF8:.4f}\n'
            f'Entropía promedio VCC: {total_entropy_VCC:.4f}\n'
            f'Entropía promedio 3OT: {total_entropy_3OT:.4f}'
        )
        self.total_entropy_label.setText(entropies_text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageSelector()
    ex.show()
    sys.exit(app.exec_())
