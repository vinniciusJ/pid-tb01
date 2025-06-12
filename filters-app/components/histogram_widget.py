from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QWidget, QVBoxLayout


class HistogramWidget(QWidget):
    def __init__(self, histogram_data, parent=None):
        super().__init__(parent)

        self.figure = Figure(figsize=(4, 3))
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.plot(histogram_data)

    def plot(self, histogram_data):
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.bar(range(len(histogram_data)), histogram_data, color="black", width=1.0)
        ax.set_title("Histograma em escala de cinza")
        ax.set_xlabel("Valor do pixel")
        ax.set_ylabel("Frequência")
        ax.set_xlim([0, 255])
        self.canvas.draw()
