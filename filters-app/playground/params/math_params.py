from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class OperationSelectWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        title = QLabel("Operação:")
        title.setFont(QFont("Ubuntu", 14))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.operation_combo = QComboBox()
        self.operation_combo.addItems(
            ["Adição", "Subtração", "Multiplicação", "Divisão"]
        )
        self.operation_combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.operation_combo.setStyleSheet("""
            QComboBox {
                background-color: #334CFF;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 6px 10px;
                font-size: 14px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 25px;
                border-left-width: 0px;
            }
            QComboBox::down-arrow {
                image: none;
                width: 0;
                height: 0;
                border-left: 6px solid transparent;
                border-right: 6px solid transparent;
                border-top: 6px solid white;
                margin-right: 6px;
            }
            QComboBox QAbstractItemView {
                background-color: #1f1f2e;
                color: white;
                selection-background-color: #3366FF;
                border: none;
                outline: none;
            }
        """)

        layout.addWidget(self.operation_combo)
        self.setLayout(layout)

    def get_selected_operation(self) -> str:
        return self.operation_combo.currentText()

    def get_params(self) -> dict:
        return {"operation": self.get_selected_operation()}
