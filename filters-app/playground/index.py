from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from style import TEXT_COLOR
from playground.left_panel import LeftPanel
from playground.right_panel import RightPanel
import cv2

from filters_registry import FILTER_REGISTRY
class Playground(QWidget):
    def __init__(self, choose_image_callback):
        super().__init__()
        self.image_path = None
        self.choose_image_callback = choose_image_callback
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        header = QLabel("FiltersApp")
        header.setFont(QFont("Ubuntu", 40, weight=50))
        header.setStyleSheet(
            f"color: rgb({TEXT_COLOR.red()}, {TEXT_COLOR.green()}, {TEXT_COLOR.blue()});  padding: 8px;"
        )
        header.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(header)

        content_layout = QHBoxLayout()
        content_layout.setAlignment(Qt.AlignCenter)

        self.left_panel = LeftPanel(self.image_path, self.choose_image_callback)
        self.right_panel = RightPanel(apply_callback=self.apply_filter)

        content_layout.addWidget(self.left_panel, 4)
        content_layout.addWidget(self.right_panel, 1)

        main_layout.addLayout(content_layout)
        self.setLayout(main_layout)

    def set_image(self, path):
        self.image_path = path
        self.left_panel.set_image(path)

    def apply_filter(self):
        if not self.image_path:
            return

        selected_filter = self.right_panel.get_selected_filter()
        params = self.right_panel.get_filter_params()
        image = cv2.imread(self.image_path)

        filter_meta = FILTER_REGISTRY.get(selected_filter)
        if filter_meta and "function" in filter_meta:
            try:
                result_image = filter_meta["function"](image, **params)
                self.left_panel.set_processed_image(result_image)
            except Exception as e:
                print(f"Erro ao aplicar filtro: {e}")
