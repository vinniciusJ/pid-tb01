from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt

from style import PRIMARY_COLOR, PRIMARY_HOVER_COLOR, PRIMARY_PRESSED_COLOR, TEXT_COLOR

class PrimaryButton(QPushButton):
    def __init__(self, text, on_click=None, width=300, height=0):
        super().__init__(text)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setMinimumSize(QSize(width, height))

        self.setStyleSheet(f"""
            PrimaryButton {{
                background-color: rgb({PRIMARY_COLOR.red()}, {PRIMARY_COLOR.green()}, {PRIMARY_COLOR.blue()}) !important;
                color: {TEXT_COLOR.name()} !important;
                font-size: 16px;
                font-weight: medium;
                padding: 12px;
                border: none;
                border-radius: 8px;
            }}
            PrimaryButton:hover {{
                background-color: rgb({PRIMARY_HOVER_COLOR.red()}, {PRIMARY_HOVER_COLOR.green()}, {PRIMARY_HOVER_COLOR.blue()}) !important;
                color: {TEXT_COLOR.name()} !important;
            }}
            PrimaryButton:pressed {{
                background-color: rgb({PRIMARY_PRESSED_COLOR.red()}, {PRIMARY_PRESSED_COLOR.green()}, {PRIMARY_PRESSED_COLOR.blue()}) !important;
                color: {TEXT_COLOR.name()} !important;
            }}
        """)

        if on_click:
            self.clicked.connect(on_click)