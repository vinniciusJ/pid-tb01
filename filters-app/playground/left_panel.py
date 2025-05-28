from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QFrame
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt
from components.text_button import TextButton
from style import PRIMARY_COLOR
from utils.clear_layout import clear_layout
import cv2

IMAGE_WIDTH = 500
IMAGE_HEIGHT = 800

class LeftPanel(QWidget):
    def __init__(self, image_path, choose_image_callback):
        super().__init__()
        self.image_path = image_path
        self.choose_image_callback = choose_image_callback
        self.original_pixmap = None
        self.processed_pixmap = None
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
        clear_layout(self.image_layout)

        if self.image_path:
            choose_button = TextButton("Escolher outra imagem", on_click=self.choose_image_callback)
            pixmap = QPixmap(self.image_path)
            self.original_pixmap = pixmap.scaled(IMAGE_WIDTH, IMAGE_HEIGHT, Qt.KeepAspectRatio)
            original_label = QLabel("Original")
            original_label.setAlignment(Qt.AlignCenter)

            self.original_image = QLabel()
            self.original_image.setPixmap(self.original_pixmap)
            self.original_image.setAlignment(Qt.AlignCenter)

            self.processed_label = QLabel("Processada")
            self.processed_label.setAlignment(Qt.AlignCenter)
            self.processed_label.hide()

            self.processed_image_view = QLabel()
            self.processed_image_view.setAlignment(Qt.AlignCenter)

            images_layout = QHBoxLayout()

            original_image_container = QVBoxLayout()
            original_image_container.addWidget(original_label)
            original_image_container.addWidget(self.original_image)

            processed_image_container = QVBoxLayout()
            processed_image_container.addWidget(self.processed_label)
            processed_image_container.addWidget(self.processed_image_view)

            images_layout.addLayout(original_image_container)
            images_layout.addLayout(processed_image_container)

            self.image_layout.addLayout(images_layout)

            self.image_layout.addWidget(choose_button)
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
        self.original_pixmap = None
        self.processed_pixmap = None
        
        if hasattr(self, "original_image"):
            self.original_image.clear()
        if hasattr(self, "processed_image_view"):
            self.processed_image_view.clear()
            self.processed_image_view.hide()
        if hasattr(self, "processed_label"):
            self.processed_label.hide()

        self.image_path = path
        self.render_image_area()

    def set_processed_image(self, image):
        height, width = image.shape[:2]
        if len(image.shape) == 2:  # grayscale
            qimage = QImage(image.data, width, height, width, QImage.Format_Grayscale8)
        else:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            qimage = QImage(image.data, width, height, width * 3, QImage.Format_RGB888)

        pixmap = QPixmap.fromImage(qimage).scaled(IMAGE_WIDTH, IMAGE_HEIGHT, Qt.KeepAspectRatio)
        self.processed_image_view.setPixmap(pixmap)

        self.processed_label.show()
