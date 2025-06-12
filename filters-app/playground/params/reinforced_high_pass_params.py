from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from components.input import Input
from playground.params.high_pass_params import HighPassParamsWidget


class ReinforcedHighPassParamsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        main_layout = QVBoxLayout(self)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setAlignment(Qt.AlignTop)

        self.high_pass_params = HighPassParamsWidget()
        content_layout.addWidget(self.high_pass_params)

        alpha_title = QLabel("Fator de reforço (α):")
        alpha_title.setFont(QFont("Ubuntu", 14))
        alpha_title.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(alpha_title)

        self.alpha_input = Input("", is_float=True)
        self.alpha_input.setRange(0.1, 10.0)
        self.alpha_input.setValue(1.5)
        content_layout.addWidget(self.alpha_input)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidget(content_widget)

        main_layout.addWidget(scroll_area)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

    def get_params(self):
        params = self.high_pass_params.get_params()
        params["alpha"] = self.alpha_input.value()
        return params
