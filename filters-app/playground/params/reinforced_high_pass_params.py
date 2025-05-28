from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from components.input import Input
from playground.params.high_pass_params import HighPassParamsWidget

class ReinforcedHighPassParamsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        self.high_pass_params = HighPassParamsWidget()
        layout.addWidget(self.high_pass_params)

        alpha_title = QLabel("Fator de reforço (α):")
        alpha_title.setFont(QFont("Ubuntu", 14))
        alpha_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(alpha_title)

        self.alpha_input = Input("", is_float=True)
        self.alpha_input.setRange(0.1, 10.0)
        self.alpha_input.setValue(1.5)
        layout.addWidget(self.alpha_input)

        self.setLayout(layout)

    def get_params(self):
        params = self.high_pass_params.get_params()
        params["alpha"] = self.alpha_input.value()
        return params
