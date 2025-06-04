import cv2

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QVBoxLayout,
    QWidget,
    QFileDialog,
)

from components.histogram_widget import HistogramWidget
from filter_type import FilterType
from filters_registry import FILTER_REGISTRY
from playground.form_panel import FormPanel
from playground.filters_panel import FiltersPanel
from style import TEXT_COLOR

header_styles = f"color: rgb({TEXT_COLOR.red()}, {TEXT_COLOR.green()}, {TEXT_COLOR.blue()});  padding: 8px;"


class Playground(QWidget):
    def __init__(self):
        super().__init__()
        self.st_image_path = None
        self.nd_image_path = None

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        header = QLabel("FiltersApp")
        header.setFont(QFont("Ubuntu", 40, weight=50))
        header.setStyleSheet(header_styles)

        header.setAlignment(Qt.AlignLeft)

        main_layout.addWidget(header)

        content_layout = QHBoxLayout()
        content_layout.setAlignment(Qt.AlignCenter)

        self.form_panel = FormPanel(
            on_st_image_button_click=self.upload_st_image,
            on_nd_image_button_click=self.upload_nd_image,
        )

        self.filters_panel = FiltersPanel(apply_callback=self.apply_filter)
        self.filters_panel.filter_selected.connect(self.on_filter_selected)

        content_layout.addWidget(self.form_panel, 4)
        content_layout.addWidget(self.filters_panel, 1)

        main_layout.addLayout(content_layout)
        self.setLayout(main_layout)

    def upload_st_image(self):
        path = self.open_image_dialog()

        if path:
            self.st_image_path = path
            self.form_panel.set_st_image(path)

    def upload_nd_image(self):
        path = self.open_image_dialog()

        if path:
            self.nd_image_path = path
            self.form_panel.set_nd_image(path)

    def apply_filter(self):
        if not self.st_image_path:
            return

        selected_filter = self.filters_panel.get_selected_filter()
        params = self.filters_panel.get_filter_params()

        image1 = cv2.imread(self.st_image_path)
        filter_meta = FILTER_REGISTRY.get(selected_filter)

        if filter_meta and "function" in filter_meta:
            try:
                if selected_filter.name == "MATH_OPERATIONS":
                    image2 = cv2.imread(self.nd_image_path)
                    params["second_image"] = image2

                result = filter_meta["function"](image1, **params)

                if selected_filter.name in ("HISTOGRAM", "HIST_EQUALIZATION"):
                    processed_image, histogram_data = result
                    self.form_panel.set_processed_image(processed_image)

                    self.histogram_window = HistogramWidget(histogram_data)
                    self.histogram_window.setWindowTitle("Histograma")
                    self.histogram_window.show()
                else:
                    self.form_panel.set_processed_image(result)

            except Exception as e:
                print(f"Erro ao aplicar filtro: {e}")
                QMessageBox.critical(self, "Erro", f"Erro ao aplicar filtro: {e}")

    def on_filter_selected(self, filter_type: FilterType):
        if filter_type == FilterType.MATH_OPERATIONS:
            self.form_panel.show_nd_image_column()
        else:
            self.form_panel.hide_nd_image_column()

    def open_image_dialog(self):
        dialog = QFileDialog(self, "Selecionar Imagem")
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Imagens (*.png *.jpg *.jpeg)")

        dialog.resize(1000, 800)

        font = QFont()
        font.setPointSize(14)
        dialog.setFont(font)

        if dialog.exec():
            selected_files = dialog.selectedFiles()
            if selected_files:
                return selected_files[0]
