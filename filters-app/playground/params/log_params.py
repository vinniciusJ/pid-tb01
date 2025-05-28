from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from components.input import Input

class LogParamsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        title = QLabel("Fator de escala (c):")
        title.setFont(QFont("Ubuntu", 14))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.c_input = Input("", is_float=True)
        self.c_input.setRange(0.1, 100.0)
        self.c_input.setSingleStep(0.1)
        self.c_input.setValue(1.0)
        layout.addWidget(self.c_input)

        self.setLayout(layout)

    def get_params(self) -> dict:
        return {"c": self.c_input.value()}
