from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QRadioButton, QButtonGroup
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from components.primary_button import PrimaryButton
from playground.params.threshold_params import ThresholdParamsWidget
from playground.params.high_pass_params import HighPassParamsWidget
from PySide6.QtWidgets import QMessageBox

from style import BG_COLOR_2

FILTERS = [
    "Limiarização", "Escala de Cinza", "Passa-Alta básico",
    "Passa-Alta Alto reforço", "Passa-Baixa Média", "Passa-Baixa Mediana",
    "Roberts", "Prewitt", "Sobel", "Log", "Zerocross",
    "Ruídos", "Watershed", "Histograma",
    "Ajuste adaptativo de histograma",
]

class RightPanel(QWidget):
    def __init__(self, get_image_path_callback=None):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        title = QLabel("Filtros disponíveis:")
        title.setFont(QFont("Ubuntu", 24, weight=50))
        main_layout .addWidget(title)

        self.filters_options_container = QWidget()
        button_layout = QVBoxLayout()
        button_layout.setContentsMargins(16, 16, 16, 16)
        button_layout.setSpacing(8)

        self.filter_button_group = QButtonGroup(self)
        self.filter_button_group.setExclusive(True)
        self.filter_button_group.idClicked.connect(self.handle_filter_id_click)

        for idx, filter_name in enumerate(FILTERS):
            radio = QRadioButton(filter_name)
            radio.setObjectName("filterRadio")
            self.filter_button_group.addButton(radio, idx)
            button_layout.addWidget(radio)

            if idx == 0:
                radio.setChecked(True)

        self.filters_options_container.setLayout(button_layout)
        self.filters_options_container.setContentsMargins(16, 16, 16, 16)
        main_layout.addWidget(self.filters_options_container)

        self.param_container = QVBoxLayout()
        main_layout.addLayout(self.param_container)

        apply_button = PrimaryButton("Aplicar filtro")
        main_layout.addWidget(apply_button)

        self.setLayout(main_layout)

        self.setStyleSheet(f"""
            QRadioButton#filterRadio {{
                background-color: rgb({BG_COLOR_2.red()}, {BG_COLOR_2.green()}, {BG_COLOR_2.blue()});
                padding: 16px;
                border: none;
                border-radius: 6px;
                font-size: 16px;
            }}
            QRadioButton#filterRadio::indicator {{
                width: 0;
                height: 0;
            }}
            QRadioButton#filterRadio:hover {{
                background-color: rgba({BG_COLOR_2.red()}, {BG_COLOR_2.green()}, {BG_COLOR_2.blue()}, 180);
            }}
            QRadioButton#filterRadio:checked {{
                background-color: rgba(100, 150, 255, 180);
                font-weight: bold;
            }}
        """)

        self.handle_filter_click(FILTERS[0])

    def handle_filter_id_click(self, id: int):
        filter_name = FILTERS[id]
        self.handle_filter_click(filter_name)

    def handle_filter_click(self, filter_name: str):
            # Limpa o param_container
            while self.param_container.count():
                child = self.param_container.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

            if filter_name == "Limiarização":
                self.param_widget = ThresholdParamsWidget()
                self.param_container.addWidget(self.param_widget)
            elif filter_name == "Passa-Alta básico":
                self.param_widget = HighPassParamsWidget()
                self.param_container.addWidget(self.param_widget)
            else:
                self.param_widget = None

