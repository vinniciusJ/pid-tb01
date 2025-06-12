import cv2

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QScrollArea,
)

from components.text_button import TextButton
from utils.clear_layout import clear_layout

IMAGE_WIDTH = 500
IMAGE_HEIGHT = 800

class FormPanel(QWidget):
    def __init__(
        self,
        on_st_image_button_click=None,
        on_nd_image_button_click=None,
    ):
        super().__init__()

        self.on_st_image_button_click = on_st_image_button_click
        self.on_nd_image_button_click = on_nd_image_button_click

        self.original_pixmap = None
        self.processed_pixmap = None
        self.additional_pixmap = None

        self.show_nd_image = False

        self.current_filter_name = None

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.scroll_area_widget = QWidget()

        self.scroll_area_layout = QHBoxLayout()
        self.scroll_area_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        self.outer_layout = QHBoxLayout(self.scroll_area_widget)
        self.outer_layout.addStretch()
        self.outer_layout.addLayout(self.scroll_area_layout)
        self.outer_layout.addStretch()

        self.scroll_area.setWidget(self.scroll_area_widget)
        self.layout.addWidget(self.scroll_area)
        self.setLayout(self.layout)

        self.render_image_area()

    def _create_image_column(
        self,
        title,
        pixmap,
        visible=True,
        placeholder_callback=None,
        change_image_callback=None,
    ):
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setAlignment(Qt.AlignCenter)

        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        image_label = QLabel()
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setFixedSize(IMAGE_WIDTH, IMAGE_HEIGHT)

        if pixmap:
            image_label.setPixmap(pixmap)
            title_label.show()
            image_label.show()
        elif placeholder_callback:
            layout.addWidget(
                TextButton("Adicionar imagem", on_click=placeholder_callback)
            )
            title_label.show()
            image_label.hide()
        else:
            title_label.hide()
            image_label.hide()

        layout.addWidget(image_label)

        if change_image_callback and pixmap:
            change_button = TextButton("Alterar imagem", on_click=change_image_callback)
            layout.addWidget(change_button)

        if not visible:
            container.hide()

        return container, image_label, title_label

    def render_image_area(self, filter_name=None):
        clear_layout(self.scroll_area_layout)

        orig_pixmap_scaled = (
            self.original_pixmap.scaled(
                IMAGE_WIDTH, IMAGE_HEIGHT, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            if self.original_pixmap
            else None
        )

        self.original_column, self.original_image_view, self.original_label_title = (
            self._create_image_column(
                "Primeira Imagem",
                orig_pixmap_scaled,
                visible=True,
                placeholder_callback=self.on_st_image_button_click,
                change_image_callback=self.on_st_image_button_click,
            )
        )

        proc_pixmap_scaled = (
            self.processed_pixmap.scaled(
                IMAGE_WIDTH, IMAGE_HEIGHT, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            if self.processed_pixmap
            else None
        )

        label_text = f"Processada ({self.current_filter_name})" if self.current_filter_name else "Processada"

        self.processed_column, self.processed_image_view, self.processed_label_title = (
            self._create_image_column(
                label_text,
                proc_pixmap_scaled,
                visible=bool(self.processed_pixmap),
            )
        )

        if self.processed_pixmap:
            empty_widget = QWidget()
            empty_widget.setFixedHeight(60)
            self.processed_column.layout().addWidget(empty_widget)

        if not self.processed_pixmap:
            self.processed_image_view.hide()
            self.processed_label_title.hide()

        add_pixmap_scaled = (
            self.additional_pixmap.scaled(
                IMAGE_WIDTH, IMAGE_HEIGHT, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            if self.additional_pixmap
            else None
        )

        (
            self.additional_column,
            self.additional_image_view,
            self.additional_label_title,
        ) = self._create_image_column(
            "Segunda imagem",
            add_pixmap_scaled,
            visible=self.show_nd_image,
            placeholder_callback=self.on_nd_image_button_click,
            change_image_callback=self.on_nd_image_button_click,
        )

        self.scroll_area_layout.addWidget(self.original_column)

        if self.show_nd_image:
            self.scroll_area_layout.addWidget(self.additional_column)

        self.scroll_area_layout.addWidget(self.processed_column)

    def show_nd_image_column(self):
        self.show_nd_image = True
        self.render_image_area()

    def hide_nd_image_column(self):
        self.show_nd_image = False
        self.render_image_area()

    def set_st_image(self, path):
        self.set_processed_image(None)

        self.original_pixmap = (
            QPixmap(path) if path and not QPixmap(path).isNull() else None
        )
        self.render_image_area()

    def set_processed_image(self, image_data, filter_name=None):
        if image_data is None:
            self.processed_pixmap = None
            self.current_filter_name = None
            self.render_image_area()
            return

        try:
            self.processed_pixmap = self._create_pixmap_from_cv_image(image_data)
            
            if filter_name:
                self.current_filter_name = filter_name

            label_text = f"Processada ({self.current_filter_name})" if self.current_filter_name else "Processada"
            self.processed_label_title.setText(label_text)

            self.render_image_area()
        except Exception as e:
            print(f"Erro ao definir imagem processada: {e}")

    def set_nd_image(self, path_or_data):
        self.set_processed_image(None)

        try:
            if isinstance(path_or_data, str):
                pixmap = QPixmap(path_or_data)
                self.additional_pixmap = pixmap if not pixmap.isNull() else None
            else:
                self.additional_pixmap = self._create_pixmap_from_cv_image(path_or_data)
            self.render_image_area()
        except Exception as e:
            print(f"Erro ao definir imagem adicional: {e}")

    def _create_pixmap_from_cv_image(self, image_data):
        height, width = image_data.shape[:2]

        if len(image_data.shape) == 2:
            format_ = QImage.Format_Grayscale8
            bytes_per_line = width
            data = image_data.data
        elif image_data.shape[2] == 3:
            image_data_rgb = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
            format_ = QImage.Format_RGB888
            bytes_per_line = width * 3
            data = image_data_rgb.data
        elif image_data.shape[2] == 4:
            image_data_rgba = cv2.cvtColor(image_data, cv2.COLOR_BGRA2RGBA)
            format_ = QImage.Format_RGBA8888
            bytes_per_line = width * 4
            data = image_data_rgba.data

        qimage = QImage(data, width, height, bytes_per_line, format_)

        return QPixmap.fromImage(qimage).scaled(
            IMAGE_WIDTH, IMAGE_HEIGHT, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
