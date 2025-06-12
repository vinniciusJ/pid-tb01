from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QScrollArea,
    QSizePolicy,
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from components.input import Input
import numpy as np


class HighPassParamsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        main_layout = QVBoxLayout(self)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)

        content_layout = QVBoxLayout(scroll_content)
        content_layout.setAlignment(Qt.AlignTop)

        title = QLabel("Kernel (3x3):")
        title.setFont(QFont("Ubuntu", 14))
        title.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(title)

        self.kernel_grid = QGridLayout()
        self.inputs = []

        for i in range(3):
            row = []
            for j in range(3):
                input_widget = Input("")
                input_widget.setRange(-10, 10)
                default_value = 8 if (i == 1 and j == 1) else -1
                input_widget.setValue(default_value)
                self.kernel_grid.addWidget(input_widget, i, j)
                row.append(input_widget)
            self.inputs.append(row)

        content_layout.addLayout(self.kernel_grid)

        main_layout.addWidget(scroll_area)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

    def get_params(self):
        kernel = np.array(
            [[self.inputs[i][j].value() for j in range(3)] for i in range(3)]
        )
        return {"kernel": kernel}
