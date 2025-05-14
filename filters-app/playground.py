from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,
    QSizePolicy, QFrame
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
from style import PRIMARY_COLOR, TEXT_COLOR
from components.text_button import TextButton

FILTERS = [
    "Limiarização (Threshold)", "Escala de Cinza", "Passa-Alta básico",
    "Passa-Alta Alto reforço", "Passa-Baixa Média (Básico)", "Passa-Baixa Mediana",
    "Roberts", "Prewitt", "Sobel", "Log", "Zerocross", "Canny Edge Detector",
    "Ruídos (salt & pepper, etc)", "Watershed", "Histograma (Escala de cinza)",
    "Ajuste adaptativo de histograma", "Contagem simples de objetos limiarizados"
]

class Playground(QWidget):
    def __init__(self, next_page_callback, choose_image_callback):
        super().__init__()
        self.next_page_callback = next_page_callback
        self.choose_image_callback = choose_image_callback
        self.image_path = None
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Header
        header = QLabel("FiltersApp")
        header.setFont(QFont("Ubuntu", 32, weight=50))
        header.setStyleSheet(f"color: rgb({TEXT_COLOR.red()}, {TEXT_COLOR.green()}, {TEXT_COLOR.blue()});  padding: 16px;")
        header.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(header)

        content_layout = QHBoxLayout()
        content_layout.setAlignment(Qt.AlignCenter)

        # Painel esquerdo
        self.left_panel = QVBoxLayout()
        self.left_panel.setAlignment(Qt.AlignTop)

        self.image_container = QWidget()
        self.image_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.image_layout = QVBoxLayout()
        self.image_layout.setAlignment(Qt.AlignCenter)
        self.image_container.setLayout(self.image_layout)

        self.render_image_area()

        self.left_panel.addWidget(self.image_container)

        # Painel direito
        right_panel = QVBoxLayout()
        right_panel.addWidget(QLabel("Filtros disponíveis:"))
        self.filter_list = QListWidget()
        for f in FILTERS:
            QListWidgetItem(f, self.filter_list)
        right_panel.addWidget(self.filter_list)

        content_layout.addLayout(self.left_panel)
        content_layout.addLayout(right_panel)

        content_layout.setStretch(0, 3)
        content_layout.setStretch(1, 2)

        main_layout.addLayout(content_layout)
        self.setLayout(main_layout)

    def render_image_area(self):
        # Limpa o layout anterior
        for i in reversed(range(self.image_layout.count())):
            widget = self.image_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        if self.image_path:
            choose_button = TextButton("Escolher outra imagem", on_click=self.choose_image_callback)

            self.image_label = QLabel()
            self.image_label.setAlignment(Qt.AlignCenter)
            self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.image_label.setScaledContents(False) 
            pixmap = QPixmap(self.image_path)
            
            pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(pixmap)

            self.image_layout.addWidget(choose_button)
            self.image_layout.addWidget(self.image_label, stretch=1)
        else:
            drop_frame = QFrame()
            drop_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            drop_frame.setStyleSheet(f"""
                QFrame {{
                    border: 2px dashed rgb({PRIMARY_COLOR.red()}, {PRIMARY_COLOR.green()}, {PRIMARY_COLOR.blue()});
                    border-radius: 8px;
                    background-color: transparent;
                }}
            """)
            
            drop_layout = QVBoxLayout()
            drop_layout.setAlignment(Qt.AlignCenter)

            choose_button = TextButton("Adicionar imagem", on_click=self.choose_image_callback)
            drop_layout.addWidget(choose_button)

            drop_frame.setLayout(drop_layout)
            self.image_layout.addWidget(drop_frame, stretch=1)


    def set_image(self, path):
        self.image_path = path
        self.render_image_area()
