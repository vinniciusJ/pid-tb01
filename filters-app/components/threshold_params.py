from PySide6.QtWidgets import QWidget, QFormLayout
from components.input import Input

class ThresholdParamsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QFormLayout()

        self.threshold_input = Input("Threshold:")
        self.threshold_input.setRange(0, 255)
        self.threshold_input.setValue(127)

        self.max_value_input = Input("Max Value:")
        self.max_value_input.setRange(0, 255)
        self.max_value_input.setValue(255)

        layout.addRow(self.threshold_input)
        layout.addRow(self.max_value_input)

        self.setLayout(layout)

    def get_values(self):
        return {
            "threshold": self.threshold_input.value(),
            "max_value": self.max_value_input.value()
        }