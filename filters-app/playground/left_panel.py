from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from components.text_button import TextButton
from style import PRIMARY_COLOR

class LeftPanel(QWidget):
    def __init__(self, image_path, choose_image_callback):
        super().__init__()
        self.image_path = image_path
        self.choose_image_callback = choose_image_callback
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)

        self.image_container = QWidget()
        self.image_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.image_layout = QVBoxLayout()
        self.image_layout.setAlignment(Qt.AlignCenter)
        self.image_container.setLayout(self.image_layout)

        self.layout.addWidget(self.image_container)
        self.setLayout(self.layout)

        self.render_image_area()

    def render_image_area(self):
        for i in reversed(range(self.image_layout.count())):
            widget = self.image_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        if self.image_path:
            choose_button = TextButton("Escolher outra imagem", on_click=self.choose_image_callback)

            self.image_label = QLabel()
            self.image_label.setAlignment(Qt.AlignCenter)
            self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.image_label.setScaledContents(False)
            pixmap = QPixmap(self.image_path)

            pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(pixmap)

            self.image_layout.addWidget(choose_button)
            self.image_layout.addWidget(self.image_label, stretch=1)
        else:
            drop_frame = QFrame()
            drop_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            drop_frame.setStyleSheet(f"""
                QFrame {{
                    border: 2px dashed rgb({PRIMARY_COLOR.red()}, {PRIMARY_COLOR.green()}, {PRIMARY_COLOR.blue()});
                    border-radius: 8px;
                    background-color: transparent;
                }}
            """)

            drop_layout = QVBoxLayout()
            drop_layout.setAlignment(Qt.AlignCenter)

            choose_button = TextButton("Adicionar imagem", on_click=self.choose_image_callback)
            drop_layout.addWidget(choose_button)

            drop_frame.setLayout(drop_layout)
            self.image_layout.addWidget(drop_frame, stretch=1)

    def set_image(self, path):
        self.image_path = path
        self.render_image_area()