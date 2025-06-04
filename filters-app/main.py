import sys

from PySide6.QtWidgets import QApplication
from style import apply_dark_theme
from playground.index import Playground


if __name__ == "__main__":
    app = QApplication(sys.argv)

    apply_dark_theme(app)

    window = Playground()

    window.setWindowTitle("Filters APP")
    window.resize(200, 200)
    window.show()
    sys.exit(app.exec())
