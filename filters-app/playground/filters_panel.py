from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QRadioButton, QButtonGroup
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, Signal

from components.primary_button import PrimaryButton
from filter_type import FilterType
from filters_registry import FILTER_REGISTRY
from style import BG_COLOR_2

FILTERS = list(FILTER_REGISTRY.keys())

class FiltersPanel(QWidget):
    filter_selected = Signal(object)

    def __init__(self, apply_callback=None):
        super().__init__()
        self.apply_callback = apply_callback
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)

        title = QLabel("Filtros disponíveis:")
        title.setFont(QFont("Ubuntu", 24, weight=50))
        main_layout.addWidget(title)

        self.filters_options_container = QWidget()
        filters_layout = QVBoxLayout()
        filters_layout.setSpacing(4)

        self.filters_button_group = QButtonGroup(self)
        self.filters_button_group.setExclusive(True)
        self.filters_button_group.idClicked.connect(self.handle_filter_id_click)

        for idx, filter_type in enumerate(FILTERS):
            radio = QRadioButton(filter_type.value)
            radio.setObjectName("filterRadio")
            self.filters_button_group.addButton(radio, idx)
            filters_layout.addWidget(radio)

            if idx == 0:
                radio.setChecked(True)

        self.filters_options_container.setLayout(filters_layout)
        self.filters_options_container.setContentsMargins(16, 16, 16, 16)
        main_layout.addWidget(self.filters_options_container)

        self.param_container = QVBoxLayout()
        main_layout.addLayout(self.param_container)

        self.apply_button = PrimaryButton(
            "Aplicar filtro", on_click=self.on_apply_clicked
        )
        main_layout.addWidget(self.apply_button)

        self.setLayout(main_layout)

        self.setStyleSheet(f"""
            QRadioButton#filterRadio {{
                background-color: rgb({BG_COLOR_2.red()}, {BG_COLOR_2.green()}, {BG_COLOR_2.blue()});
                padding: 12px;
                border: none;
                border-radius: 6px;
                font-size: 15px;
            }}
            QRadioButton#filterRadio::indicator {{
                width: 0;
                height: 0;
            }}
            QRadioButton#filterRadio:hover {{
                background-color: rgba({BG_COLOR_2.red()}, {BG_COLOR_2.green()}, {BG_COLOR_2.blue()}, 180);
            }}
            QRadioButton#filterRadio:checked {{
                background-color: rgba(100, 150, 255, 180);
                font-weight: bold;
            }}
        """)

        self.handle_filter_click(FILTERS[0])

    def on_apply_clicked(self):
        if self.apply_callback:
            self.apply_callback()

    def get_selected_filter(self) -> FilterType:
        checked_button = self.filters_button_group.checkedButton()
        if not checked_button:
            return None
        return FilterType.from_label(checked_button.text())

    def get_filter_params(self) -> dict:
        if hasattr(self, "param_widget") and self.param_widget:
            return self.param_widget.get_params()
        return {}

    def handle_filter_id_click(self, id: int):
        filter_type = FILTERS[id]
        self.handle_filter_click(filter_type)

        self.filter_selected.emit(filter_type)

    def handle_filter_click(self, filter_type: FilterType):
        while self.param_container.count():
            child = self.param_container.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        self.param_widget = None
        filter_meta = FILTER_REGISTRY.get(filter_type)

        if filter_meta and "widget" in filter_meta:
            self.param_widget = filter_meta["widget"]()
            self.param_container.addWidget(self.param_widget)
