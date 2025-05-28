from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSpinBox, QDoubleSpinBox
from style import BG_COLOR_2
from PySide6.QtGui import QFont

class Input(QWidget):
    def __init__(self, label_text, parent=None, is_float=False):
        super().__init__(parent)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(label_text)
        self.label.setFont(QFont("Ubuntu", 14))
        layout.addWidget(self.label)

        self.is_float = is_float
        if self.is_float:
            self.spinbox = QDoubleSpinBox()
            self.spinbox.setDecimals(2)  # Pode ajustar o número de casas decimais se quiser
        else:
            self.spinbox = QSpinBox()

        self.spinbox.setStyleSheet(
            f"""
            QSpinBox, QDoubleSpinBox {{
                background-color: rgb({BG_COLOR_2.red()}, {BG_COLOR_2.green()}, {BG_COLOR_2.blue()});
                color: white;
                font-size: 12pt;
            }}
            """
        )
        layout.addWidget(self.spinbox)

    def setRange(self, min_val, max_val):
        self.spinbox.setRange(min_val, max_val)

    def setSingleStep(self, step):
        self.spinbox.setSingleStep(step)

    def setValue(self, value):
        self.spinbox.setValue(value)

    def value(self):
        return self.spinbox.value()
