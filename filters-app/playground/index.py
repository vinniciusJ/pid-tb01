from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from style import TEXT_COLOR
from playground.left_panel import LeftPanel
from playground.right_panel import RightPanel

class Playground(QWidget):
    def __init__(self, next_page_callback, choose_image_callback):
        super().__init__()
        self.image_path = None
        self.next_page_callback = next_page_callback
        self.choose_image_callback = choose_image_callback
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Header
        header = QLabel("FiltersApp")
        header.setFont(QFont("Ubuntu", 40, weight=50))
        header.setStyleSheet(f"color: rgb({TEXT_COLOR.red()}, {TEXT_COLOR.green()}, {TEXT_COLOR.blue()});  padding: 16px;")
        header.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(header)

        content_layout = QHBoxLayout()
        content_layout.setAlignment(Qt.AlignCenter)

        self.left_panel = LeftPanel(self.image_path, self.choose_image_callback)
        self.right_panel = RightPanel()

        content_layout.addWidget(self.left_panel, 3)
        content_layout.addWidget(self.right_panel, 2)

        main_layout.addLayout(content_layout)
        self.setLayout(main_layout)

    def set_image(self, path):
        self.image_path = path
        self.left_panel.set_image(path)