from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from components.primary_button import PrimaryButton

from style import BG_COLOR_2, DROP_ZONE_BORDER_COLOR

FILTERS = [
    "Limiarização (Threshold)", "Escala de Cinza", "Passa-Alta básico",
    "Passa-Alta Alto reforço", "Passa-Baixa Média (Básico)", "Passa-Baixa Mediana",
    "Roberts", "Prewitt", "Sobel", "Log", "Zerocross", "Canny Edge Detector",
    "Ruídos (salt & pepper, etc)", "Watershed", "Histograma (Escala de cinza)",
    "Ajuste adaptativo de histograma", "Contagem simples de objetos limiarizados"
]

class RightPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setContentsMargins(16, 16, 16, 16)

        title = QLabel("Filtros disponíveis:")
        title.setFont(QFont("Ubuntu", 24, weight=50))
        main_layout .addWidget(title)

        filters_options_container = QWidget()
        button_layout = QVBoxLayout()
        button_layout.setContentsMargins(16, 16, 16, 16)
        button_layout.setSpacing(8)

        for filter_name in FILTERS:
            button = QPushButton(filter_name)
            button.setObjectName("filterButton")
            # button.clicked.connect(lambda checked, name=filter_name: self.handle_filter(name))
            button_layout .addWidget(button)

        filters_options_container.setLayout(button_layout)
        main_layout.addWidget(filters_options_container)

        apply_button = PrimaryButton("Aplicar filtro")
        main_layout.addWidget(apply_button)

        self.setLayout(main_layout)

        self.setStyleSheet(f"""
            QPushButton#filterButton {{
                background-color: rgb({BG_COLOR_2.red()}, {BG_COLOR_2.green()}, {BG_COLOR_2.blue()});
                padding: 16px;
                border: none;
                border-radius: 6px;
                text-align: left;
                font-size: 16px;
            }}
            QPushButton#filterButton:hover {{
                background-color: rgba({BG_COLOR_2.red()}, {BG_COLOR_2.green()}, {BG_COLOR_2.blue()}, 180);
            }}
        """)
