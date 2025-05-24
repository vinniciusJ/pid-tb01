from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from style import TEXT_COLOR
from playground.left_panel import LeftPanel
from playground.right_panel import RightPanel
import cv2
from filters.grayscale import grayscale
from filters.thresholding import thresholding
from filters.basic_high_pass import high_pass
from filters.basic_low_pass import mean_low_pass
from filters.median import median_filter

from filter_type import FilterType


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

        result_image = None

        match selected_filter:
            case FilterType.THRESHOLDING:
                threshold = params.get("threshold", 127)
                max_value = params.get("max_value", 255)
                result_image = thresholding(image, threshold, max_value)

            case FilterType.GRAYSCALE:
                result_image = grayscale(image)

            case FilterType.HIGH_PASS:
                kernel = params.get("kernel")
                result_image = high_pass(image, kernel)

            case FilterType.HIGH_BOOST:
                result_image = None

            case FilterType.LOW_PASS_MEAN:
                result_image = mean_low_pass(image)

            case FilterType.LOW_PASS_MEDIAN:
                result_image = median_filter(image)

            case FilterType.ROBERTS:
                # result_image = roberts(image)
                result_image = None
                # TODO

            case FilterType.PREWITT:
                # result_image = prewitt(image)
                result_image = None
                # TODO

            case FilterType.SOBEL:
                # result_image = sobel(image)
                result_image = None
                # TODO

            case FilterType.LOG_TRANSFORM:
                result_image = None
                # TODO

            case FilterType.HISTOGRAM:
                result_image = None
                # TODO

            case FilterType.HIST_EQUALIZATION:
                result_image = None
                # TODO

            case _:
                result_image = None

        if result_image is not None:
            self.left_panel.set_processed_image(result_image)
