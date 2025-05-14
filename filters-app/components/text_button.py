from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt

from style import PRIMARY_COLOR, PRIMARY_HOVER_COLOR, PRIMARY_PRESSED_COLOR, TEXT_COLOR

class TextButton(QPushButton):
    def __init__(self, text, on_click=None, width=300, height=60):
        super().__init__(text)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setMinimumSize(QSize(width, height))

        self.setStyleSheet(f"""
            TextButton {{
                background-color: transparent !important;
                color: {PRIMARY_COLOR.name()} !important;
                font-size: 18px;
                font-weight: medium;
                padding: 0;
                border: none;
                border-radius: 8px;
            }}
            TextButton:hover {{
                background-color: transparent !important;
                color: {PRIMARY_HOVER_COLOR.name()} !important;
            }}
            TextButton:pressed {{
                background-color: transparent !important;
                color: {PRIMARY_PRESSED_COLOR.name()} !important;
            }}
        """)

        if on_click:
            self.clicked.connect(on_click)