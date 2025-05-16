from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSpinBox
from style import BG_COLOR_2
from PySide6.QtGui import QFont

class Input(QWidget):
    def __init__(self, label_text, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(label_text)
        self.label.setFont(QFont("Ubuntu", 14))
        layout.addWidget(self.label)

        self.spinbox = QSpinBox()
        self.spinbox.setStyleSheet(
            f"""
            QSpinBox {{
                background-color: rgb({BG_COLOR_2.red()}, {BG_COLOR_2.green()}, {BG_COLOR_2.blue()});
                color: white;
                font-size: 12pt;
                padding: 8px;
            }}
            """
        )
        layout.addWidget(self.spinbox)

    def setRange(self, min_val, max_val):
        self.spinbox.setRange(min_val, max_val)

    def setValue(self, value):
        self.spinbox.setValue(value)

    def value(self):
        return self.spinbox.value()