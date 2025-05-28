from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from components.input import Input

class LowPassParamsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        title = QLabel("Tamanho do kernel (ímpar):")
        title.setFont(QFont("Ubuntu", 14))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.kernel_input = Input("", is_float=False) 
        self.kernel_input.setRange(1, 15)
        self.kernel_input.setSingleStep(2) 
        self.kernel_input.setValue(3)
        layout.addWidget(self.kernel_input)

        self.setLayout(layout)

    def get_params(self) -> dict:
        return {"kernel_size": self.kernel_input.value()}
